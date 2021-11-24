L = [15 ,7, 27, 39]
p = int(input("Digite um dos valores a procurar: "))
v = int(input("Digite o outro valor a procurar: "))
contador = 0
achado = {p:0,v:0}
while contador < len(L):
    if p == L[contador]:
        achado[p] = contador
    elif v == L[contador]:
        achado[v] = contador
    contador += 1
if achado[p] == 0 and achado[v] == 0:
    print(f"{p} e {v} não encontrados")
elif achado[p] == achado[v]:
    print(f"{p} e {v} foram encontrados na posicação {achado[p]}")
elif achado[p] < achado[v]:
    print(f"{p} foi achado primeiro na posição {achado[p]}")
    print(f"{v} foi achado em seguida na posição {achado[v]}")
else:
    print(f"{v} foi achado primeiro na posição {achado[v]}")
    print(f"{p} foi achado em seguida na posição {achado[p]}")