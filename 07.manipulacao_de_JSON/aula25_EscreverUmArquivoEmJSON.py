import json

telefone = {
    "produto": "Celular",
    "preco": 1200,
    "estoque": 50
}

with open("telefone.json", "w", encoding="utf-8") as f:
    #        (dicionário, as, número de linhas que irá usar, mantém os acentos normais)
    json.dump(telefone, f, indent=4, ensure_ascii=False)