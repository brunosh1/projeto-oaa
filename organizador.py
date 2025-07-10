import os
import shutil
import time
#caminho da pasta que será organizada
caminho_origem= r"C:\Users\bruno\Downloads"
#dicionário que mapeia extexões para pastas
mapa_pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "ArquivosCompactados": [".zip", ".rar", ".7z", ".tar.gz"],
    "Executáveis": [".exe", ".msi"],
}
#lista todos os caminhos e pastas no diretório
try:
    lista_de_arquivos= os.listdir(caminho_origem)
except FileNotFoundError:
    print(f"Erro : O caminho '{caminho_origem}' não foi encontrado. Verifique o caminho e tente novamente")
    exit()
#loop principal que percorre cada item da pasta origem
for arquivo in lista_de_arquivos:
    caminho_completo_arquivo=os.path.join(caminho_origem, arquivo) #caminho completo para o aquivo
    if os.path.isfile(caminho_completo_arquivo):#verifica se o item atual é um arquivo e não uma pasta
        
        nome_arquivo, extensao=os.path.splitext(arquivo)#pega a extensão do arquivo em minúsculas
        extensao=extensao.lower()
        if not extensao:#se não tiver extensão, pula para o próximo arquivo
            continue
        pasta_destino=None #encontra a pasta de destino com base na extensão

        for pasta, extensoes in mapa_pastas.items():
            if extensao in extensoes:
                pasta_destino = pasta
                break
        if pasta_destino is None: #se a extensão não estiver no nosso mapa, podemos criar uma pasta outros
            pasta_destino="Outros"

        caminho_pasta_destino=os.path.join(caminho_origem, pasta_destino) # Cria o caminho completo da pasta de destino

        if not os.path.exists(caminho_pasta_destino):# Cria o caminho completo da pasta de destino
            print(f"Criando pasta: {pasta_destino}")
            os.makedirs(caminho_pasta_destino)

        try: #move o arquivo para a pasta de destino
            print(f"Movendo '{arquivo}' para pasta '{pasta_destino}'...")
            shutil.move(caminho_completo_arquivo, caminho_pasta_destino)
            
        except Exception as e:
            print(f"Não foi possível mover o arquivo '{arquivo}'. Erro {e}")

print("\nOrganização concluída com sucesso!")