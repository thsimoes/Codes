while True:
    numero = input("Qual número você que saber se é palindromo? ")
    if numero == "0":
        break
    contador1 = 0
    contador2 = -1
    palindromo = True
    while contador1 < len(numero)//2:
        if numero[contador1] != numero[contador2]:
            palindromo = False
            break
        else:
            contador1 += 1
            contador2 -= 1
    if palindromo:
        print("Esse número é palindromo!")
    else:
        print("Esse número não é palindromo!")
    print("\n")