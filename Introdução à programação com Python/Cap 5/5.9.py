contador = 0
x = int(input("Qual é o dividendo? "))
dividendo = x
y = int(input("Qual é o divisor? "))
while x >= y:
    x -= y
    contador += 1
print(f"O resultado da divisão inteira é {contador} e o resto é {x}")