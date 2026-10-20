import json
import sys
import urllib.request

# windows abre o terminal em cp1252, ai acento sai zoado sem isso
sys.stdout.reconfigure(encoding="utf-8")

cep = input("Digite o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = urllib.request.urlopen(url)
dados = json.loads(resposta.read())

print(f"{dados['logradouro']}, {dados['bairro']}")
print(f"{dados['localidade']} - {dados['uf']}")
