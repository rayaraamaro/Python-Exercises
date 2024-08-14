#JOGO DA VELHA

def player_input():

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Jogador 1, ecolha X ou O: ').upper()

    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def display_board(board):

    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|---|--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|---|--')
    print(board[1]+' | '+board[2]+' | '+board[3])

def place_marker(board, marker, position):
    board[position] = marker


def space_check(board, position):
    return board[position] not in ['X', 'O']


def check_win(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

def tic_tac_toe():
    print('Bem-vindo ao Jogo da Velha!')
    board = ['#'] + [' '] * 9  
    player1_marker, player2_marker = player_input()
    
    for turn in range(9):  
        display_board(board)
        if turn % 2 == 0:
            current_marker = player1_marker
            print("Vez do Jogador 1")
        else:
            current_marker = player2_marker
            print("Vez do Jogador 2")
        
        position = 0
        while position not in range(1, 10) or not space_check(board, position):
            position = int(input('Escolha uma posição (1-9): '))

        place_marker(board, current_marker, position)

        if check_win(board, current_marker):
            display_board(board)
            print(f'Jogador {1 if turn % 2 == 0 else 2} venceu!')
            return
    
    display_board(board)
    print('Empate!')

tic_tac_toe()