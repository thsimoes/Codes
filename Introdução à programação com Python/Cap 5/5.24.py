é_primo = 1
print("Teste dos primos até o seu número: ")
limite = int(input("Qual seu número? "))
primo = 0
while primo <= limite:
    if primo == 2 or primo == 3:
        print(primo)
        primo += 1
        continue
    contador = 2
    while contador <= primo//2:
        divisor = (primo/contador == primo//contador)
        if divisor:
            break
        else:
            if contador == 2:
                contador += 1
            else:
                contador += 2
        if contador > primo//2:
            print(primo)
    primo += 1