import requests

from coleta_dados_web import requisicao


def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = 'C:\\Users\\SERGIO\\Desktop\\EBAC\\produtos_informatica.xlsx'

    # Enviar arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={'file': open(caminho, 'rb')})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado. Link para acesso:", url)

def enviar_arquivo_chave():
    # Caminho do Arquivo e chave para upload
    caminho = 'C:\\Users\\SERGIO\\Desktop\\EBAC\\produtos_informatica.xlsx'
    chave_acesso = 'iJrMKziKXSNe4gZy6sNr8yls7FjozVNB'  #API token key

    # Enviar o arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadFile',
                               files={'file': open(caminho, 'rb')},
                               headers={'Authorization': chave_acesso}
                               )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['data']['downloadPage']
    print("Arquivo enviado com chave. Link para acesso:", url)

def receber_arquivo(file_url):
    # receber arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo:", requisicao.json())

enviar_arquivo()
enviar_arquivo_chave()
# receber_arquivo(https://upload.gofile.io/uploadFile)
