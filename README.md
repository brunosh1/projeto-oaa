Script de Organização Automática de Arquivos
Este projeto foi desenvolvido para facilitar a vida de quem, como eu, costuma acumular muitos arquivos na pasta de Downloads.
Com ele, você pode organizar seus arquivos automaticamente, separando-os em pastas como Imagens, Documentos, Vídeos, Compactados e outros, de acordo com o tipo de cada arquivo.

Sobre o projeto
A ideia surgiu da necessidade pessoal de manter minha pasta de Downloads mais limpa e funcional.
Com este script feito em Python, o processo é totalmente automatizado: ele verifica a extensão dos arquivos e move cada um para a pasta correspondente. Se a pasta não existir, o script cria na hora.

O objetivo é deixar o dia a dia mais prático, sem precisar organizar manualmente dezenas de arquivos.

Funcionalidades
Detecta a extensão dos arquivos automaticamente

Move cada arquivo para a pasta apropriada

Cria pastas novas se elas ainda não existirem

Fácil de personalizar (você pode incluir novas extensões e categorias)

Evita mover pastas ou arquivos inválidos

Tecnologias utilizadas
Python 3

Bibliotecas padrão:

os

shutil

time

Como usar
Requisitos
Ter o Python 3 instalado no seu computador com Windows

Passo a passo
Clone este repositório ou baixe o arquivo do script:

bash
Copiar
Editar
git clone https://github.com/brunoherminio/organizador-downloads.git
Abra o arquivo organizador.py e configure o caminho da pasta que você quer organizar. Por padrão, ele já vem com a pasta Downloads:

python
Copiar
Editar
caminho_origem = r"C:\Users\bruno\Downloads"
Abra o terminal (Git Bash, PowerShell ou o terminal do VS Code)

Vá até a pasta onde está o script:

bash
Copiar
Editar
cd caminho/para/o/script
Execute o script:

nginx
Copiar
Editar
python organizador.py
Pronto! Os arquivos da pasta de origem serão organizados automaticamente.

Melhorias planejadas
Adicionar uma interface gráfica simples para facilitar o uso

Permitir passar o caminho da pasta como argumento no terminal

Criar um registro de arquivos movidos (log)

Incluir opção de desfazer a última movimentação

Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar.

Desenvolvido por Bruno Hermínio
Estudante de Análise e Desenvolvimento de Sistemas
Contato: linkedin.com/in/brunoherminio
