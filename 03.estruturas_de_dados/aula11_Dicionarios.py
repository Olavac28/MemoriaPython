#precisa de bastante ""
pessoa = {
    "nome": "João",
    "idade": 20,
    "peso": 73
}
print(pessoa)

print(pessoa["nome"]) #printra o atributo "nome"
pessoa["nome"] = "Pedro"
print(pessoa["nome"])

pessoa["altura"] = 180 #adiciona um novo atributo
print(pessoa["altura"])

del pessoa["idade"] #exclui um atributo
print(pessoa)
pessoa.clear() #excli tudo do dicionário
print(pessoa)
del pessoa #exclui o dicinário