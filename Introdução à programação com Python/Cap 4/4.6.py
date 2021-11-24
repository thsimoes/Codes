
distancia = float(input("Qual a distância percorrida? "))
valor = 0
if distancia > 200:
    valor =  distancia*0.45
else:
    valor = distancia*0.5
print(f"O valor a ser pago pela viagem é {valor:.2f}")