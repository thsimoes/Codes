cigarro_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fuma? "))
tempo = anos*365*cigarro_dia*10//(60*24)
print(f"A redução do seu tempo de vida fumando {cigarro_dia} cigarros por dia ao logo dos {anos} anos é equivalente a {tempo} dias.")