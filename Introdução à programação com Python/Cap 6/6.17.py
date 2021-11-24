estoque = {"tomate":[100,2.3],
            "alface":[500,0.45],
            "batata" : [2001,1.2],
            "feijão" : [100,1.5]}
produto = input("Qual foi o produto vendido? ")
quantidade = int(input("Qual foi a quantidade vendida? "))
venda = [produto, quantidade]
total = 0
print("Vendas:\n")
while produto in estoque:
    preço = estoque[produto][1]
    custo = quantidade*preço
    print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}\n")
    estoque[produto][0] -= quantidade
    total += custo
    produto = input("Qual foi o produto vendido? ")
    if produto in estoque:
        quantidade = int(input("Qual foi a quantidade vendida? "))
print(f"\nCusto total: {total:21.2f}\n")
for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")