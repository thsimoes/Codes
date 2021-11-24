valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 100
a_pagar = valor
while True:
    if valor == 0:
        print("0 cédula(s) de R$ 100")
        print("0 cédula(s) de R$ 50")
        print("0 cédula(s) de R$ 20")
        print("0 cédula(s) de R$ 10")
        print("0 cédula(s) de R$ 5")
        print("0 cédula(s) de R$ 1")
        break
    if atual <= a_pagar:
        a_pagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cédula(s) de R$ {atual}")
        if a_pagar == 0:
            break
        if atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0