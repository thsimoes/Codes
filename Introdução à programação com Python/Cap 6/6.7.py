from typing import overload


parenteses = input("Digite uma expressão com parênteses: ")
contador = 0
fim = len(parenteses)
pilha = []
expressão = []
while contador < fim:
    expressão.append(parenteses[contador])
    contador += 1
contador = 0
while contador < fim:
    if expressão[0] == "(":
        pilha.append("(")
        expressão.pop(0)
    else:
        expressão.pop(0)
        if len(pilha) > 0:
            pilha.pop(-1)
        else:
            pilha.append(")")
            break
    contador += 1
if len(pilha) == 0:
    print("A expressão está correta!")
elif len(pilha) > 0:
    print("Erro")