import os
import glob
import PyPDF2

# Função de Inicialização:
def init():
    print("Iniciando separador de PDF's")

    diretorio = "nao_processados"
    padrao_pdf = os.path.join(diretorio, '*.pdf')
    arquivos_pdf = glob.glob(padrao_pdf)

    if(len(arquivos_pdf) == 0):
        print("Nenhum arquivo para ser processado")
    else:
        processar_arquivos(arquivos_pdf)

# Função para percorrer multiplos arquivos na pasta nao_processados
def processar_arquivos(arquivos):
    print("Iniciando processador de PDF's")
    
    for arquivo in arquivos:
        processar_pdf(arquivo)


def processar_pdf(arquivo):
    pdf_reader = PyPDF2.PdfReader(arquivo)
    print(pdf_reader.pages)

    for page_num in range(len(pdf_reader.pages)):
            # Obtém o texto da página
            page = pdf_reader.pages[page_num]
            texto_na_pagina = page.extract_text()

            linhas = texto_na_pagina.splitlines()
            nome_linha = linhas[11]

            # Cria um novo PDF com uma única página
            nome_final = tratarNome(nome_linha)
            novo_pdf = f"separados/{nome_final}.pdf"

            output = PyPDF2.PdfWriter()
            output.add_page(pdf_reader.pages[page_num])
            with open(novo_pdf, "wb") as outputStream:
                 output.write(outputStream)

def tratarNome(nome):
    corte = nome.find(' ')
    nomeFinal = nome[corte:]
    return nomeFinal
      
init()