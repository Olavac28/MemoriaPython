'''
    variáveis dinamicas
    e de tipagem fraca
'''

nome = "hans"
print(nome)

n1 = n2 = 2 #ambas valem 2
print(n1 + n2)

n3, n4 = 3, 4 #uma vale 3 e a outra vale 4
print(n3 + n4)

print(type(nome)) #mostra o tipo
print(type(1 + 2j)) #outro tipo de dado

print(isinstance(n1, int)) #verifica de a variável é de um tipo especifico