L = [15 ,7, 27, 39]
p = int(input("Digite o valor a procurar: "))
contador = 0
while contador < len(L):
    if p == L[contador]:
        print(f"{p} achado na posição {contador}")
        break
    elif contador == len(L) - 1:
        print(f"{p} não encontrado!")
    contador += 1