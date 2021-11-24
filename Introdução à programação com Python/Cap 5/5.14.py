soma = 0
contador = 0
while True:
    n = int(input("Digite um número para que eu grave ou 0 para sair: "))
    if n == 0:
        break
    soma += n
    contador += 1
print("\n")
print(f"Foram digitados {contador} números")
print(f"A soma desses {contador} números é igual a {soma}")
print(f"A média desses {contador} números é igual a {soma/contador:.2f}")
print("\n")