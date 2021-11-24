divida = float(input("Qual é o valor da sua dívida? "))
divida_restante = divida
juros = float(input("Qual a taxa de juros dessa dívida? "))
mensal = float(input("Qual valor da dívida você pagará mensalmente? "))
pago = 0
juros_pago = 0
while divida_restante > 0:
    if mensal <= divida_restante:
        juros_pago += (juros/100)*divida_restante
        divida_restante += (juros/100)*divida_restante
        divida_restante -= mensal
        pago += mensal
        meses = divida_restante//mensal
        if divida_restante/mensal != divida_restante//mensal:
            meses = divida_restante//mensal + 1
        print("\n")
        print(f"Você ainda precisa pagar a dívida por mais {int(meses)} meses")
        print(f"Já foram pagos R$ {pago:.2f}")
        print(f"E o juros já representam um somatório de R$ {juros_pago:.2f}")
    else:
        juros_pago += (juros/100)*divida_restante
        divida_restante += (juros/100)*divida_restante
        pago += divida_restante
        divida_restante = 0
        meses = divida_restante//mensal
        if divida_restante/mensal != divida_restante//mensal:
            meses = divida_restante//mensal + 1
        print("\n")
        print(f"Você ainda precisa pagar a dívida por mais {int(meses)} meses")
        print(f"Já foram pagos R$ {pago:.2f}")
        print(f"E o juros já representam um somatório de R$ {juros_pago:.2f}")
print("\n")