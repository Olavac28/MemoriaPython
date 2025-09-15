try:
    senhaPin = int(input("Digite a senha: "))
    print("senha válida")
except: #caso nn colocado nada na frente, o interpretador considera qualque erro
    print("senha inválida")