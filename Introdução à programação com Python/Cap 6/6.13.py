lista = [-10,-8,0,1,2,5,-2,-4]
min = lista[0]
max = lista[0]
soma = 0
contador = 0
for i in lista:
    if i > max:
        max = i
    if i < min:
        min = i
    soma += i
    contador += 1
print(f"Menor = {min}")
print(f"Maior = {max}")
print(f"Média = {soma/contador:.2f}")