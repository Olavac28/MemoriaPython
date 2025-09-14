def org(original):
    temp = original.copy() #cria um cópia; se fiser direto, temp só ficará apontada para original
    original.clear() #apaga todos os itens de uma lista

    for i in range(len(temp)):
        menor = min(temp)
        temp.remove(menor) #remove a primeira ocorrencia na lista
        original.append(menor)

lista = [4, 5, 4, 2, 6, 1]
org(lista)
print(lista)