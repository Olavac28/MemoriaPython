#for item in sequencia:
lista = [1, 2, 3, 4]
for item in lista: #para cada item na lista:
    print(item)

palavra = "abobrinha"
for letra in palavra:
    print(letra)

for numero in range(0, 10): #vai de 0 a 9
    print(numero)

for x in range(5): #já cmç no 0
    print(x)

#             (inicio, fim, incremento)
for y in range(0, 22, 2):
    print(y)

lang = ("C", "C++", "Java", "Python")
for lang in lang:
    if (lang == "Python"):
        continue
    print(lang)