import random

#                     (menor, maior)
valor = random.randint(1, 5)
print(valor)

lista = [1, 2, 4, 6]
n = random.choice(lista)
print(n)
n = random.sample(lista, 3) #escole 3 valores de uma lista
print(n)