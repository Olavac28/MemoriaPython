import json

JSONstring = '{"nome": "Ana", "idade": 25, "cidades": ["SP", "RJ"]}'
pessoa = json.loads(JSONstring) #de string para dicionário
print(pessoa)

JSONstring2 = json.dumps(pessoa)
print(JSONstring2) #de dicionário para string