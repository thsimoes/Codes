preço = float(input("Qual é o o valor do produto? "))
desconto = float(input("Qual é o percentual de desconto será aplicado? "))
preço *= 1 - desconto/100
print(f"Com {desconto:.2f}% de desconto, o novo preço do produto será {preço}")