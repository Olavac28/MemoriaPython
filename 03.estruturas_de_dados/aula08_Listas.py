l1 = [1, 2, 3]
l2 = [4, 5, 6]
lista = l1 + l2 #junta as listas
print(lista)

print(lista[0]) #mostra o primeiro indice
print(lista[-1]) #mostra o ultimo indice

print(len(lista)) #mostra o tamanho da lista
print(sorted(lista, reverse=True)) #mostra a lista invertida
print(sum(lista)) #soma toda a lista
print(min(lista)) #encontra o menor valor
print(max(lista)) #encontra o maior valor

lista.append(7) #adiciona um valor à lista
print(lista)

lista.pop(-1) #remove um valor da lista com base no i
print(lista)

lista.insert(4, 4.5)
print(lista)

lista.remove(4.5) #remove o primeiro valor 4.5 da lista

print(17 in lista) #verifica se existe o número na lista

#matriz
l3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(l3[1][2])

bebidas = []
for i in range(3):
    bebidas.append(input(f"qual sua bebida n{i}: "))
for b in bebidas:
    print(b)