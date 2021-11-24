print("Menu:")
print("  Adição (A)")
print("  Subtração (S)")
print("  Divisão (D)")
print("  Multiplicação (M)")
print("  Sair (0)")
escolha = "a"
opções = {"A":"Adição","a":"Adição","S":"Subtração","s":"Subtração","D":"Divisão","d":"Divisão","M":"Multiplicação","m":"Multiplicação"}
while True:
    escolha = input("Qual tabuada você deseja realizar? ")
    if escolha == "0":
        break
    elif escolha not in opções:
        print("Escolha uma opção de tabuada válida no menu.")
    else:
        tabuada = 1
        while tabuada < 10:
            multiplicador = 1
            while multiplicador < 10:
                if opções[escolha] == "Adição":
                    print(f"{opções[escolha]}: {tabuada} + {multiplicador} = {tabuada+multiplicador}")
                elif opções[escolha] == "Subtração":
                    print(f"{opções[escolha]}: {tabuada} - {multiplicador} = {tabuada-multiplicador}")
                elif opções[escolha] == "Divisão":
                    print(f"{opções[escolha]}: {tabuada} / {multiplicador} = {tabuada/multiplicador:.2f}")
                elif opções[escolha] == "Multiplicação":
                    print(f"{opções[escolha]}: {tabuada} x {multiplicador} = {tabuada*multiplicador}")
                multiplicador += 1
            tabuada += 1
