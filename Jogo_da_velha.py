jogo = [0,0,0,
        0,0,0,
        0,0,0]

def Vitoria(jogo, num, jogador):

    if jogo[0] == num and jogo[1] == num and jogo[2] == num or jogo[3] == num and jogo[4] == num and jogo[5] == num or jogo[6] == num and jogo[7] == num and jogo[8] == num:
        print("vitoria do " + jogador)
        return 1

    elif jogo[0] == num and jogo[3] == num and jogo[6] == num or jogo[1] == num and jogo[4] == num and jogo[7] == num or jogo[2] == num and jogo[5] == num and jogo[8] == num:
        print("vitoria do " + jogador)
        return 1

    elif jogo[0] == num and jogo[4] == num and jogo[8] == num or jogo[2] == num and jogo[4] == num and jogo[6] == num:
        print("vitoria do " + jogador)
        return 1

    else:
        
        if jogo[0] != 0 and jogo[1] != 0 and jogo[2] != 0 and jogo[3] != 0 and jogo[4] != 0 and jogo[5] != 0 and jogo[6] != 0 and jogo[7] != 0 and jogo[8] != 0:
            print("Empate")
            return 1
        
        else:
            return 0

def Jogada(jogo, num, jogador):

    print(jogador)
    posicao = int(input("Qual posição: "))

    for quadrado in range(0, len(jogo)):

        if quadrado == posicao:
            if jogo[quadrado] == 0:
                jogo[quadrado] = num
                return 0
            else:
                print("Posição já utilizada")
                Jogada(jogo, num, jogador)

def Imagem_jogo(jogo):
    print(f'{jogo[0]} {jogo[1]} {jogo[2]}')
    print(f'{jogo[3]} {jogo[4]} {jogo[5]}')
    print(f'{jogo[6]} {jogo[7]} {jogo[8]}')

def main(): 

    Jogador = []
    Jogador.append(input("nome do Jogador 1: "))
    Jogador.append(input("nome do Jogador 2: "))

    while 0 == 0 :

        for num_jogador in range(0, len(Jogador)):
            Jogada(jogo, num_jogador+1, Jogador[num_jogador])
            Imagem_jogo(jogo)
            resultado = Vitoria(jogo, num_jogador+1, Jogador[num_jogador])

            if resultado == 1:
                exit()
            
main()