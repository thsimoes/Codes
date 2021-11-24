def tamanho(a,b,c):
    if len(a) >= b and len(a) <= c:
        return True
    else:
        return False

print(tamanho("Tiago",3,8))
print(tamanho("Tiago",6,8))