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
    print("CEP inválido, precisa ter 8 números (pode usar ou não o hífen)")
else:
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    try:
        resposta = urllib.request.urlopen(url, timeout=5)
        dados = json.loads(resposta.read())
    except urllib.error.URLError:
        print("Não foi possível conectar na API, verifique a internet")
    else:
        if dados.get("erro"):
            print("CEP não encontrado")
        else:
            print(f"{dados['logradouro']}, {dados['bairro']}")
            print(f"{dados['localidade']} - {dados['uf']}")
