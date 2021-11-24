ultimo1 = 10
ultimo2 = 10
fila1 = list(range(1,ultimo1 + 1))
fila2 = list(range(1,ultimo2 + 1))
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F ou A para adicionar ou atender um cliente na fila 1, respectivamente")
    print("Digite G ou B para adicionar ou atender um cliente na fila 2, respectivamente")
    print("ou S para sair.")
    operação = input("Operação (F, G, A, B ou S): ")
    contador = 0
    if operação == "S":
        break
    while contador < len(operação):
        if contador > 0:
            print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} clientes na fila 2")
            print(f"Fila 1 atual: {fila1}")
            print(f"Fila 2 atual: {fila2}")
        if operação[contador] == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido na fila 1")
            else:
                print("Fila 1 vazia! Ninguém para atender.")
        elif operação[contador] == "F":
            ultimo1 += 1
            fila1.append(ultimo1)
        elif operação[contador] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido na fila 2")
            else:
                print("Fila 2 vazia! Ninguém para atender.")
        elif operação[contador] == "G":
            ultimo2 += 1
            fila2.append(ultimo2)
        elif operação[contador] == "S":
            break
        else:
            print(f"Operação {operação[contador]} inválida! Digite apenas F, A ou S!")
        contador += 1
    if operação[contador] == "S":
        break