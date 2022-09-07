from ast import If
from datetime import date
import webbrowser
from googletrans import Translator 
import requests

trad = Translator()
today = date.today()

dia = today.strftime('%d')
mouth = today.strftime('%B')
mes = trad.translate(mouth,dest="pt").text
ano = today.strftime('%Y')

a = 0

while a < 1:
    a = a + 1
    b = str(a)
    num = b.zfill(4)
    url = f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{mes}/{dia}/exec1/pdf/pg_{num}.pdf'
    #webbrowser.open(url)


def baixar_pdf(url ,endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open (endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
if __name__ == "__main__":

    baixar_pdf(url, 'pag_00001')



# print(f'http://diariooficial.imprensaoficial.com.br/doflash/prototipo/{ano}/{mes}/{dia}/exec1/pdf/pg_0001.pdf')
#         # http://diariooficial.imprensaoficial.com.br/doflash/prototipo/2022/Setembro/07/exec1/pdf/pg_0001.pdf

# print(url)
# webbrowser.open(url)
