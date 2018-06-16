import requests
import json

url = "https://www.bec.sp.gov.br/BEC_API/API/pregaoM/NegociacaoItemOC"
headers = {}
response = requests.request("GET", url, headers=headers)

extraction = json.loads(response.text)

print(type(extraction))
