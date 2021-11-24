def primo(a):
    i = 2
    if a == 1 or a == 0:
        é_primo = False
    else:
        é_primo = True
        while i <= a/2:
            if a % i == 0:
                é_primo = False
            i += 1
    return é_primo

def primos_intervalo(valor):
    lista = []
    for i in range(valor):
        if primo(i):
            lista.append(i)
    return lista

def mdc(a,b):
    lista = primos_intervalo(b)
    divisores = []
    valor = 1
    for i in lista:
        while a % i == 0 and b % i == 0:
            a, b = a / i, b / i
            divisores.append(i)
    for j in divisores:
        valor *= j
    return valor

def mdc_rec(a,b):
    if b == 0:
        return a
    else:
        x =  a % b
        a = b
        b = x
        return mdc_rec(a,b)

print(mdc_rec(60,12))
print(mdc_rec(63,12))
print(mdc_rec(17,5))