dias = int(input("Quantos dias? "))
horas = int(input("Quantos horas? "))
minutos = int(input("Quantos minutos? "))
segundos = int(input("Quantos segundos? "))
total = dias*24*3600 + horas*3600 + minutos*60 + segundos
print(f"{dias} dias {horas} horas {minutos} minutos e {segundos} segundos totalizam {total} segundos.")
