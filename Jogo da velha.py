def imprime(lista):
    for i in range(len(lista)):
        print(f" {trans[lista[i][0]]} | {trans[lista[i][1]]} | {trans[lista[i][2]]}")
        if i < (len(lista) - 1):
            print("---+---+---")
        else:
            print()
def pos(posição):
    if posição == 1:
        return [2,0]
    elif posição == 2:
        return [2,1]
    elif posição == 3:
        return [2,2]
    elif posição == 4:
        return [1,0]
    elif posição == 5:
        return [1,1]
    elif posição == 6:
        return [1,2]
    elif posição == 7:
        return [0,0]
    elif posição == 8:
        return [0,1]
    elif posição == 9:
        return [0,2]
    elif posição > 9 or posição < 1:
        return False
def troca(posição,lista,jogador):
        a, b = pos(posição)
        lista[a][b] = jogador
def ganhou(lista):
    if lista[1][1] != 0:
        if lista[0][0] == lista[1][1] and lista[0][0] == lista[2][2]:
            return True
        elif lista[0][2] == lista[1][1] and lista[0][2] == lista[2][0]:
            return True
    for i in range(len(lista)):
        if lista [i][i] != 0:
            if lista[i][0] == lista[i][1] and lista[i][0] == lista[i][2]:
                return True
            elif lista[0][i] == lista[1][i] and lista[0][i] == lista[2][i]:
                return True
    return False

exemplo = [[7,8,9],[4,5,6],[1,2,3]]
jogo = [[0,0,0],[0,0,0],[0,0,0]]
trans = {0:" ",1:"X",2:"O"}

#imprimindo as diversas posições possíveis
print("\nAs posições possíveis do jogo da velha estão enumeradas a seguir:\n")
for i in range(len(exemplo)):
        print(f" {exemplo[i][0]} | {exemplo[i][1]} | {exemplo[i][2]}")
        if i < (len(exemplo) - 1):
            print("---+---+---")

#imprimindo como está o tabuleiro
print("\nVamos começar!\n")
imprime(jogo)

#preencher o tabuleiro
ganhador = False

while not ganhador:
    jogador = 1
    while jogador < 3:
        escolha = int(input(f"Jogador {jogador}: Qual posição você escolhe? "))
        a,b = pos(escolha)
        if jogo[a][b] == 0:
            troca(escolha,jogo,jogador)
            print("O jogo está assim: ")
            print()
            imprime(jogo)
            if ganhou(jogo):
                print(f"O jogador {jogador} ganhou!\n")
                ganhador = True
                break
            else:
                jogador += 1
        else:
            print(f"Posição inválida! Tente novamente jogador {jogador}")
        if 0 not in jogo[0] and 0 not in jogo[1] and 0 not in jogo[2]:
            print("Velha!\n")
            ganhador = True
            break
