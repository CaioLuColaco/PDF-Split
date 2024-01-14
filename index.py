import os
import glob

def init():
    print("Iniciando separador de PDF's")

    diretorio = "nao_processados"
    padrao_pdf = os.path.join(diretorio, '*.pdf')
    arquivos_pdf = glob.glob(padrao_pdf)

    if(len(arquivos_pdf) == 0):
        print("Nenhum arquivo para ser processado")
    else:
        processar_pdfs(arquivos_pdf)

def processar_pdfs():
    print("Iniciando processador de PDF's")
    
init()