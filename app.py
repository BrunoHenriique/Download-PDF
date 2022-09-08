#                                               IMPORTS
from csv import reader
import PyPDF2
from ast import If
from datetime import date
import webbrowser
from googletrans import Translator 
import requests

#                                               TRATAMENTO DE DATA
trad = Translator()
today = date.today()

# dia = today.strftime('%d')
# mouth = today.strftime('%B')
# mes = trad.translate(mouth,dest="pt").text
# ano = today.strftime('%Y')

dia = '07'
mes = 'Setembro'
ano = '2022'

#                                               MANIPULAÇÃO DO LINK PDF
a = 0
while a < 1:
    a = a + 1
    b = str(a)
    num = b.zfill(4)
    url = f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{mes}/{dia}/exec1/pdf/pg_{num}.pdf'
    #webbrowser.open(url)

#                                               FUNÇÃO DOWNLOAD DO PDF
def baixar_pdf(url ,endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open (endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

a = 0
while a < 2:
    a = a + 1
    b = str(a)
    num = b.zfill(4)
    baixar_pdf(url, f'pag_{num}')
#                                               TRATAMENTO DE PDF
    pdf = open(f'pag_{num}', 'rb')
    reader = PyPDF2.PdfFileReader(pdf)
    pagina = reader.getPage(0)

    print(f'-==--=-=-=-=-=-=-=-=-==--=-=-=-PAGINA PAG_{num} -==--=-=-=-=-=-=-=-=-==--=-=-=-')
    print(pagina.extractText())
    