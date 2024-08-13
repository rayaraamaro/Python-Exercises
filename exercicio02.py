#Jogo da Velha 

#addX = []
#addO = []

'''def add_X_or_O():
    while True:  
        usuario_input = input("Insira qual forma deseja jogar, X ou O: ").upper()
        
        if usuario_input == 'X':
            return "Você escolheu X!"
        elif usuario_input == 'O':
            return "Você escolheu O!"
        else:
            print("Valor inválido, por favor insira a forma correta!")  
    
print(add_X_or_O())'''
game_list = [0, 1, 2]

def display_game(game_list):
    print('Aqui esta a lista: ')
    print(game_list)

def position_choice():
    choice = "wrong"
    number = ['0', '1', '2']

    while choice not in number:

        choice = input ("Escolha uma posição (0, 1, 2): ")

        if choice not in number:
            print('Escolha inválida, desculpe! ')

    return int(choice)

print(position_choice())

def replacement_choice(game_list, position):
    user_placement = input("Digite um X ou O para colocar na posição: ")
    
    game_list[position]= user_placement

    return game_list

print(replacement_choice(game_list,1))

def gameon_choice():

    choice = "wrong"

    while choice not in [ 'S', 'N']:
        choice = input('Quer continuar jogando? (S ou N): ').upper()
        
        if choice not in ['S', 'N']:
            print("Desculpe, não entendi, por favor escolha S ou N: ")
    
    if choice == "S":
        return True
    else:
        return False
    
game_on = True

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()

#criar uma forma para colocar os indices
#adicionar o input relacionado ao indice

'''def jogo(row1, row2, row3):
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    
    jogador01 = int(input('Em qual linha deseja jogar 1, 2 ou 3? '))
    if jogador01 == row1:
        row1.append[]'''
