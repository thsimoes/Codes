km = float(input("Quantos km você rodou com o carro? "))
dias = int(input("Por quantos dias você ficou com o carro? "))
preço = 0.15*km + 60*dias
print(f"O valor que deve ser pago é R${preço:.2f}")
