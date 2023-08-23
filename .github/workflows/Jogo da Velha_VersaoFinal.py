from random import randrange

def tabela_jogo(quadrado):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(quadrado[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(quadrado):
    ok = False  # suposição falsa - precisamos dela para entrar no loop
    while not ok:
        move = input("Digite o número do seu movimento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'  # a entrada do usuário é válida?
        if not ok:
            print("Número inexistente! Favor digite um valor de 1 a 9!")  # Quando a jogada estiver fora do intervalo
            continue
        move = int(move) - 1  # número da célula de 0 a 8
        row = move // 3  # linha da célula
        col = move % 3  # coluna da célula
        sign = quadrado[row][col]  # verifique o quadrado selecionado
        ok = sign not in ['O', 'X']
        if not ok:  # está ocupado - pare a entrada novamente
            print("Campo já ocupado - repita sua entrada!")

    quadrado[row][col] = 'O'  # definir 'O' no quadrado selecionado

def make_list_of_free_fields(quadrado):
    free = []  # a lista está vazia inicialmente
    for row in range(3):  # iterar pelas linhas
        for col in range(3):  # iterar pelas colunas
            if quadrado[row][col] not in ['O', 'X']:  # a célula está livre?
                free.append((row, col))  # sim, está - anexar nova tupla à lista
    return free

def victory_for(quadrado, sgn):
    if sgn == "X":  # estamos procurando por X?
        who = 'me'  # sim - é o lado do computador
    elif sgn == "O":  # ... ou para O?
        who = 'you'  # sim - é o nosso lado
    else:
        who = None  # não deveríamos cair aqui!

    cross1 = cross2 = True  # para diagonais
    for rc in range(3):
        if quadrado[rc][0] == sgn and quadrado[rc][1] == sgn and quadrado[rc][2] == sgn:  # verificar linha rc
            return who
        if quadrado[0][rc] == sgn and quadrado[1][rc] == sgn and quadrado[2][rc] == sgn:  # verificar coluna rc
            return who
        if quadrado[rc][rc] != sgn:  # verificar 1ª diagonal
            cross1 = False
        if quadrado[2 - rc][2 - rc] != sgn:  # verificar 2ª diagonal
            cross2 = False

    if cross1 or cross2:
        return who

    return None

def draw_move(quadrado):
    free = make_list_of_free_fields(quadrado)  # faça uma lista de campos livres
    cnt = len(free)
    if cnt > 0:  # se a lista não estiver vazia, escolha um lugar para 'X' e configure-o
        this = randrange(cnt)
        row, col = free[this]
        quadrado[row][col] = 'X'

quadrado = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # fazer um tabuleiro vazio
quadrado[1][1] = 'X'  # definir primeiro 'X' no meio
free = make_list_of_free_fields(quadrado)
human_turn = True  # qual turno é agora?

while len(free):
    tabela_jogo(quadrado)
    if human_turn:
        enter_move(quadrado)
        victor = victory_for(quadrado, 'O')
    else:
        draw_move(quadrado)
        victor = victory_for(quadrado, 'X')

    if victor != None:
        break

    human_turn = not human_turn
    free = make_list_of_free_fields(quadrado)

tabela_jogo(quadrado)

if victor == 'you':
    print("Parabéns, Você ganhou do computador!")
elif victor == 'me':
    print("O Computador Venceu, mas não desanime, continue treinando!")
else:
    print("Empate, o jogo foi muito disputado!")
