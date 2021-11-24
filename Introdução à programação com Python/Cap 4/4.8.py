a = float(input("Qual o primeiro número? "))
b = float(input("Qual o segundo número? "))
print("Digite os seguintes comandos para escolher um dos 4 tipos de operação:")
print(" + , caso deseje somar;")
print(" - , caso deseje subtrair;")
print(" * , caso deseje multiplicar;")
print(" / , caso deseje dividir.")
op = input("Qual operação você deseja realizar? ")
if op == "+":
    print(f"O resultado da soma é: {a+b:.2f}")
elif op == "-":
    print(f"O resultado da subtração é: {a-b:.2f}")
elif op == "*":
    print(f"O resultado da multiplicação é: {a*b:.2f}")
elif op == "/":
    print(f"O resultado da divisão é: {a/b:.2f}")
else:
    print("A operação solicitada não existe.")