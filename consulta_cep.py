import json
import re
import sys
import urllib.error
import urllib.request

# windows abre o terminal em cp1252, ai acento sai zoado sem isso
sys.stdout.reconfigure(encoding="utf-8")

cep = input("Digite o CEP: ")
cep_limpo = re.sub(r"\D", "", cep)

if len(cep_limpo) != 8:
    print("CEP invalido, precisa ter 8 numeros (pode usar ou nao o hifen)")
else:
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    try:
        resposta = urllib.request.urlopen(url, timeout=5)
        dados = json.loads(resposta.read())
    except urllib.error.URLError:
        print("Nao foi possivel conectar na API, verifique a internet")
    else:
        if dados.get("erro"):
            print("CEP nao encontrado")
        else:
            print(f"{dados['logradouro']}, {dados['bairro']}")
            print(f"{dados['localidade']} - {dados['uf']}")
