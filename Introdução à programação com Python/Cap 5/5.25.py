print("Bem-vindo a calculadora de raízes!")
print("Basta digitar o número que deseja saber a raiz quadrada ou digitar x para sair")
while True:
    n = input("Qual o número que você deseja saber a raiz? ")
    if n == "x" or n == "X":
        break
    n = float(n)
    b = 2
    p = 0
    while abs(p**2 - n) > 0.0001:
        p = (b + (n/b))/2
        b = p
    print(f"{p:.4f}")