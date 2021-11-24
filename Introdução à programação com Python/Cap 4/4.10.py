consumo = float(input("Qual foi a quantidade de kWh consumida? "))
print("Qual o seu tipo de instalação? Selecione uma das opções a seguir: ")
print(" R , para residências;")
print(" I , para indústrias;")
print(" C , para comércios.")
tipo = input("Qual o seu tipo de instalação? ")
if tipo == "r" or tipo == "R":
    if consumo < 500:
        print(f"O preço a pagar pelo fornecimento de energia elétrica é R$ {consumo*0.4:.2f}")
    else:
        print(f"O preço a pagar pelo fornecimento de energia elétrica é R$ {consumo*0.65:.2f}")
elif tipo == "c" or tipo == "C":
    if consumo < 1000:
        print(f"O preço a pagar pelo fornecimento de energia elétrica é R$ {consumo*0.55:.2f}")
    else:
        print(f"O preço a pagar pelo fornecimento de energia elétrica é R$ {consumo*0.60:.2f}")
elif tipo == "i" or tipo == "I":
    if consumo < 5000:
        print(f"O preço a pagar pelo fornecimento de energia elétrica é R$ {consumo*0.55:.2f}")
    else:
        print(f"O preço a pagar pelo fornecimento de energia elétrica é R$ {consumo*0.60:.2f}")
else:
    print("O seu tipo de instalação não foi informado corretamente!")