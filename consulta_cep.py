import json
import re
import sys
import urllib.request

# windows abre o terminal em cp1252, ai acento sai zoado sem isso
sys.stdout.reconfigure(encoding="utf-8")

cep = input("Digite o CEP: ")
cep_limpo = re.sub(r"\D", "", cep)

if len(cep_limpo) != 8:
    print("CEP invalido, precisa ter 8 numeros (pode usar ou nao o hifen)")
else:
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    resposta = urllib.request.urlopen(url)
    dados = json.loads(resposta.read())

    print(f"{dados['logradouro']}, {dados['bairro']}")
    print(f"{dados['localidade']} - {dados['uf']}")
