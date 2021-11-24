soma = 0
while True:
    print("\n")
    print("Caso deseje adicionar compras, digite o código do produto")
    print("Já caso queira finalizar a compra digite 0")
    print("\n")
    codigo = int(input("Qual é o código do produto? "))
    codigos_validos = {1:0.5,2:1,3:4,5:7,9:8}
    if codigo == 0:
        break
    elif codigo in codigos_validos:
        soma += codigos_validos[codigo]
    else:
        print("\n")
        print("Código inválido")
print("\n")
print(f"Sua compra deu um total de R$ {soma:.2f}")
print("\n")