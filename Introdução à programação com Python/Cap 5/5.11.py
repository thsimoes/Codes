deposito_inicial = float(input("Qual o valor do depósito inicial? "))
valor_atual = deposito_inicial
taxa = float(input("Qual é a taxa de juros dessa poupança? "))
contador = 1
while contador <= 24:
    valor_atual *= 1 + taxa/100
    print(f"Mês {contador}: Você possui R$ {valor_atual:.2f}")
    contador += 1
print(f"O valor total ganho com juros nesse período foi R$ {valor_atual - deposito_inicial:.2f}")