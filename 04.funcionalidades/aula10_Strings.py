frase = "Ola eu sou o"

print(frase.split()) #transforma uma frase em um lista de palavras
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

print(frase.replace("Ola", "Opa"))

email = input("Digite seu email: ")
verifica = email.find('@') #pega o número do array da string
if (email[verifica:verifica+10] == "@gmail.com"):
    print("email válido")
else:
    print("email inválido")