notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota {x+1} = "))
    soma += notas[x]
    x += 1
x = 0
while x < 7:
    print(f"Notas {x+1} = {notas[x]:.2f}")
    x += 1
print(f"Média: {soma/x:.2f}")