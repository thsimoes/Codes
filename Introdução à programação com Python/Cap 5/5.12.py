deposito_inicial = float(input("Qual o valor do depósito inicial? "))
valor_atual = deposito_inicial
taxa = float(input("Qual é a taxa de juros dessa poupança? "))
contador = 1
deposito_mensal = float(input("Qual será o seu depósito mensal? "))
while contador <= 24:
    if contador != 1:
        valor_atual += deposito_mensal
    valor_atual *= 1 + taxa/100
    print(f"Mês {contador}: Você possui R$ {valor_atual:.2f}")
    contador += 1
print(f"O valor total ganho com juros nesse período foi R$ {valor_atual - (deposito_inicial + deposito_mensal*23):.2f}")