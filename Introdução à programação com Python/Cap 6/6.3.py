lista = [[],[]]
x = 0
while x < 2:
    y = 0
    while True:
        n = float(input(f"Qual é o valor {y} da sua lista {x+1} (digite 0 para ir para próxima lista): "))
        if n == 0:
            break
        lista[x].append(n)
        y +=1
    x += 1
x = 0
lista1 = []
while x < 2:
    y = 0
    while y < len(lista[x]):
        if lista[x][y] not in lista1:
            lista1.append(lista[x][y])
        y += 1
    x += 1
print(lista1)