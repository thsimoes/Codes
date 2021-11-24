é_primo = 1
print("Teste dos primos: ")
print("(Caso deseje parar os testes digite X)")
while True:
    é_primo = input("Qual número você gostaria de saber que é primo? ")
    if é_primo == "X" or é_primo == "x":
        break
    é_primo = int(é_primo)
    if é_primo == 0 or é_primo == 1:
        print("Não é primo!")
    elif é_primo == 2 or é_primo == 3:
        print("É primo!")
    else:
        divisor = 2
        while divisor <= é_primo//2:
            teste = é_primo % divisor
            if teste == 0:
                print("Não é primo!")
                break
            else:
                if divisor == 2:
                    divisor += 1
                else:
                    divisor += 2
            if divisor > é_primo//2:
                print("É primo!")

        