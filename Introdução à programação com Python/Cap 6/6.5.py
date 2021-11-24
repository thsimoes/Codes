ultimo = 10
fila = list(range(1,ultimo + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação (F, A ou S): ")
    contador = 0
    if operação == "S":
        break
    while contador < len(operação):
        if contador > 0:
            print(f"\nExistem {len(fila)} clientes na fila")
            print(f"Fila atual: {fila}")
        if operação[contador] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[contador] == "F":
            ultimo += 1
            fila.append(ultimo)
        elif operação[contador] == "S":
            break
        else:
            print(f"Operação {operação[contador]} inválida! Digite apenas F, A ou S!")
        contador += 1
    if operação[contador] == "S":
        break