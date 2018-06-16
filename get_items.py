import requests
import json

url = "https://www.bec.sp.gov.br/BEC_API/API/pregaoM/NegociacaoItemOC"
headers = {}
response = requests.request("GET", url, headers=headers)

extraction = json.loads(response.text)

situacoes = set()

# {'ANÁLISE DE RECURSOS', 'AGUARDANDO PRAZO ABERTURA SESSÃO PÚBLICA-RETOMADA', 'PREGÃO SUSPENSO', 'EDITAL PUBLICADO', 'PRAZO PARA MEMORIAIS', 'AGUARDANDO RECEBIMENTO DE PROPOSTAS', 'AGUARDANDO ABERTURA SESSÃO PÚBLICA-RETOMADA', 'ADJUDICAÇÃO AUTORIDADE', 'ELABORAÇÃO DA ATA', 'PRAZO PARA CONTRARRAZÕES', 'HOMOLOGAÇÃO'}

situacao = 'EDITAL PUBLICADO'

for item in extraction:
    url = "https://www.bec.sp.gov.br/BEC_API/API/pregaoM/NegociacaoItemOC/{}".format(item['Codigo'])
    response = requests.request("GET", url, headers=headers)
    ocs = json.loads(response.text)

    for oc in ocs:
        situacoes.add(oc['SITUACAO'])
        if situacao == oc['SITUACAO']:
            print(oc)

print(situacoes)
