salario = float(input("Qual é o seu salário? "))
aumento = 0
if salario > 1250:
    aumento = 0.1*salario
    print(f"O seu aumento será de R$ {aumento:.2f}.")
else:
    aumento = 0.15*salario
    print(f"O seu aumento será de R$ {aumento:.2f}.")
