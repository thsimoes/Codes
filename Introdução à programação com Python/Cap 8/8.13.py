from typing import List

def valida(a,b):
    if type(b) == List:
        for i in range(len(b)):
            b[i] = b[i].lower()
    else:
        b = b.lower()
    if a.lower() in b:
        return True
    else:
        return False

lista = "A"
while True:
    if not valida(input("Digite uma opção: "), lista):
        print()
        print("Tente outra vez!\n")
    else:
        print()
        break