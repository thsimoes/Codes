valor = float(input("Qual é o valor da casa? "))
salario = float(input("Qual é o seu salário? "))
anos =  int(input("Por quantos anos você deseja pagar essa casa? "))
meses = anos*12
mensalidade = valor / meses
if mensalidade > 0.3*salario:
    print("O empréstimo foi negado, pois o valor mensal da prestação é superior a 30% do seu salário.")
else:
    print(f"O empréstimo foi aprovado e você pagará {meses} parcelas de R$ {mensalidade:.2f}")