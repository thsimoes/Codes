dist = float(input("Qual é a distância a ser percorrida? "))
velocidade = float(input("Qual será sua velocidade média? "))
horas = int(dist/velocidade)
minutos = int((dist/velocidade - horas)*60)
segundos = int(((dist/velocidade - horas)*60 - minutos)*60)
print(f"Essa viagem irá durar {horas} horas, {minutos} minutos e {segundos} segundos")