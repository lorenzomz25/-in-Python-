
tabela = [' '] * 10
rodada = 1
n1 = 0
n2 = 0


# função para imprimir a tabela a cada movimento;
def imprimeTabela():
    print(tabela[1], '|', tabela[2], '|', tabela[3])
    print("----------")
    print(tabela[4], '|', tabela[5], '|', tabela[6])
    print("----------")
    print(tabela[7], '|', tabela[8], '|', tabela[9])
    print()



#   função para verificar se um dos jogadores é o vencedor.
def vencedor(jogador):
    if (((tabela[1] == tabela[2] == tabela[3] == "X") or (tabela[1] == tabela[2] == tabela[3] == "O")) or
        ((tabela[4] == tabela[5] == tabela[6] == "X") or (tabela[4] == tabela[5] == tabela[6] == "O")) or
        ((tabela[7] == tabela[8] == tabela[9] == "X") or (tabela[7] == tabela[8] == tabela[9] == "O")) or
        ((tabela[1] == tabela[4] == tabela[7] == "X") or (tabela[1] == tabela[4] == tabela[7] == "O")) or
        ((tabela[2] == tabela[5] == tabela[8] == "X") or (tabela[2] == tabela[5] == tabela[8] == "O")) or
        ((tabela[3] == tabela[6] == tabela[9] == "X") or (tabela[3] == tabela[6] == tabela[9] == "O")) or
        ((tabela[1] == tabela[5] == tabela[9] == "X") or (tabela[1] == tabela[5] == tabela[9] == "O")) or
        ((tabela[3] == tabela[5] == tabela[9] == "X") or (tabela[3] == tabela[5] == tabela[9] == "O"))):
        print("-------------------------------------")
        print("Jogador %d é o vencedor!!!" % jogador)
        print("-------------------------------------")
        return 1 #



#   faz a jogada do jogador 1 e imprime a tabela.
def jogador_1():
    print("Jogador 1")

    n1 = int(input("Informe o numero correspondente ao espaço da tabela: "))
    while ((1 > n1) or (n1 > 9) or (n1 == n2) or (tabela[n1] != ' ')):
        # o "and tabeça[n1] == '' " evita que o mesmo jogador digite uma posição já informada por ele.
        # Ex: o jogador 1 digita 5 na primeira rodada e novamente 5 na quarta rodada.
        n1 = int(input("Informe o numero correspondente ao espaço da tabela: "))
    tabela[n1] = "X"
    imprimeTabela()



#   faz a jogada do jogador 2 e imprime a tabela.
def jogador_2():
    print("Jogador 2")

    n2 = int(input("Informe o numero correspondente ao espaço da tabela: "))
    while ((1 > n2) or (n2 > 9) or (n2 == n1) or (tabela[n2] != ' ')):
        n2 = int(input("Informe o numero correspondente ao espaço da tabela: "))
    tabela[n2] = "O"
    imprimeTabela()




print("----------------------------------------------------------")
print("\t\t\t\t\t  JOGO DA VELHA")
print("----------------------------------------------------------\n")


while rodada <= 5:
    print()
    print("\t\t\t\t\t\tRODADA %d\n" % rodada)

    jogador_1()

    if vencedor(1) == 1:
        break

    #   o programa é interrompido após a ultima jogada do jogador 1 na rodada 5
    #   ja que o jogador 1 jogará mais vezes que o jogador 2, pelo fato da tabela possuir um numero impar de casas,
    #   o jogo será interrompido após a 9ª jogada.
    if (rodada == 5):
        if vencedor(1) != 1 and vencedor(2) != 1:
            print("-------------------------------------")
            print("\t\t\tEmpatado!!!")
            print("-------------------------------------")
        break
    #   caso contrário...
    else:
        jogador_2()

        if vencedor(2) == 1:
            break

    rodada = rodada + 1