# Consulta CEP

Script em Python que pede um CEP, consulta a API publica do ViaCEP e mostra o
endereco. Valida o formato antes de consultar e trata CEP inexistente e falha
de conexao.

## O que pratiquei

- `urllib.request` para fazer uma requisicao GET sem instalar nada
- `json.loads` para transformar a resposta em dicionario
- `re.sub` para limpar o CEP digitado (com ou sem hifen)
- `try/except urllib.error.URLError` para erro de rede
- `sys.stdout.reconfigure` pra nao bugar acento no terminal do Windows

## Como rodar

```
python consulta_cep.py
```

Digite o CEP quando pedir, com ou sem hifen.
