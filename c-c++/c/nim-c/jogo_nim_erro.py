def partida(pontos_usuario, pontos_computador):
    print("")
    print("pontos_usuario")
    print("pontos_computador")
    print("**** Rodada 1 ****")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (m + 1) % n == 0:
        return usuario_escolhe_jogada(n, m, pontos_usuario, pontos_computador)
    else:
        return computador_escolhe_jogada(n, m, pontos_usuario, pontos_computador)

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    pontos_usuario = 0
    pontos_computador = 0
    print("1 - para jogar uma partida isolada ")
    jogo = int(input("2 - para jogar um campeonato\n>"))
    if jogo == 1:
        print("")
        print("Voce escolheu uma partida!")
        return partida(pontos_usuario, pontos_computador)
    else:
        print("")
        print("Voce escolheu um campeonato!")
        return campeonato(pontos_usuario, pontos_computador)

def usuario_escolhe_jogada(n, m, pontos_usuario, pontos_computador):
    print("")
    print("Voce começa!")
    print("")
    jogada = True
    while n >= m and jogada:
        x = int(input("Quantas peças você vai tirar? "))
        if x > m and x == 0:
            print("Oops! Jogada inválida! Tente de novo.")
            return usuario_escolhe_jogada(n, m)
        if x == 1:
            print("Você tirou uma peça.")
        if x > 1:
            print("Você tirou", x, "peças.")
        n = n - x
        if m >= x:
            jogada = False
    if n == 0:
        pontos_usuario = pontos_usuario + 1
        print("Fim do jogo! Voce ganhou!")
    else:
        if n > 1:
            print("Agora restam", n, "peças no tabuleiro.")
            return computador_escolhe_jogada(n, m, pontos_usuario, pontos_computador)
        else:
            print("Agora resta apenas uma peça no tabuleiro")
            return computador_escolhe_jogada(n, m, pontos_usuario, pontos_computador)

def computador_escolhe_jogada(n, m, pontos_usuario, pontos_computador):
    print("")
    print("Computador começa!")
    print("")
    x = n % (m + 1)
    if x > 1:
        print("O computador tirou", x, "peças.")
    if x == 1:
        print("O computador tirou uma peça.")
    n = n - x
    if n == 0:
        pontos_computador = pontos_computador + 1
        print("Fim do jogo! O computador ganhou!")
    else:
        if n > 1:
            print("Agora restam", n, "peças no tabuleiro.")
            return usuario_escolhe_jogada(n, m, pontos_usuario, pontos_computador)
        else:
            print("Agora resta apenas uma peça no tabuleiro")
            return usuario_escolhe_jogada(n, m, pontos_usuario, pontos_computador)

def partida2(pontos_usuario, pontos_computador):
    print("pontos_computador")
    print("pontos_usuario")
    print("**** Rodada 2 ****")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (m + 1) % n == 0:
        return usuario_escolhe_jogada(n, m, pontos_usuario, pontos_computador)
    else:
        return computador_escolhe_jogada(n, m, pontos_usuario, pontos_computador)

def partida3(pontos_usuario, pontos_computador):
    print("pontos_computador")
    print("pontos_usuario")
    print("**** Rodada 3 ****")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (m + 1) % n == 0:
        return usuario_escolhe_jogada(n, m, pontos_usuario, pontos_computador)
    else:
        return computador_escolhe_jogada(n, m, pontos_usuario, pontos_computador)

def campeonato(pontos_usuario, pontos_computador):
    print(partida(pontos_usuario, pontos_computador))
    print(partida2(pontos_usuario, pontos_computador))
    print(partida3(pontos_usuario, pontos_computador))
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você", pontos_usuario, "X", pontos_computador, "Computador")

if __name__ == "__main__":
    main()