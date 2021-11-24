L = ["x"]
for i in L:
    n = int(input("Digite um número (0 sai): "))
    if n == 0:
        break
    L.append(n)
del(L[0])
for j in L:
    print(j)