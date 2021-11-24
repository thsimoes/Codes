while True:
    continua = input("Você deseja continuar? (s/n) ")
    if continua == "n":
        break
    dividendo = int(input("Qual o dividendo? "))
    divisor = int(input("Qual o divisor? "))
    memoria = dividendo
    resto = 0
    while divisor <= dividendo:
        dividendo -= divisor
    print(f"O resto da divisão inteira de {memoria} por {divisor} é {dividendo}")