frase = input("Qual a sua frase? ")
letras = {}
for i in frase:
    if i in letras:
        letras[i] += 1
    else:
        letras[i] = 1
print(letras)