a = float(input("O primeiro valor é: "))
b = float(input("O segundo valor é: "))
c = float(input("O terceiro valor é: "))
if a > b and a > c and b > c:
    print(f"O maior valor é {a:.2f} e o menor valor é {c:.2f}")
elif a > b and a > c and c > b:
    print(f"O maior valor é {a:.2f} e o menor valor é {b:.2f}")
elif b > a and b > c and a > c:
    print(f"O maior valor é {b:.2f} e o menor valor é {c:.2f}")
elif b > a and b > c and c > a:
    print(f"O maior valor é {b:.2f} e o menor valor é {a:.2f}")
elif c > b and c > a and a > b:
    print(f"O maior valor é {c:.2f} e o menor valor é {b:.2f}")
elif c > b and c > a and b > a:
    print(f"O maior valor é {c:.2f} e o menor valor é {a:.2f}")