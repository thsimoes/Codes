def pesq(lista,valor):
    if valor in lista:
        return lista.index(valor)
    return None

lista = [10,20,25,30]
print(pesq(lista,25))
print(pesq(lista,27))