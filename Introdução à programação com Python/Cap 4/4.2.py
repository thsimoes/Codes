velocidade =  int(input("A qual velocidade seu carro está? "))
multa = 0
if velocidade > 80:
    velocidade -= 80
    multa = float(velocidade*5)
    print(f"Você foi multado no valor de R$ {multa:.2f}.")
else:
    print("Você não foi multado.")