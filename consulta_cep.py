import json
import urllib.request

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = urllib.request.urlopen(url)
dados = json.loads(resposta.read())

print(dados)
