salario = float(input("Qual é o seu salario? "))
aumento = float(input("Qual é o percentual de aumento que será dado? "))
salario *= 1 + aumento/100
print(f"Com {aumento:.2f}% de aumento, seu novo salário será {salario}")