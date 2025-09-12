n = 10;

while (n > 0):
    print(n)
    n -= 1

while True:
    esc = input()
    if (esc == "x"):
        print("saindo...")
        break
    print("!!!")