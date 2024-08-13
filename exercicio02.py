#Jogo da Velha 

#addX = []
#addO = []

def add_X_or_O():
    while True:  
        usuario_input = input("Insira qual forma deseja jogar, X ou O: ").upper()
        
        if usuario_input == 'X':
            return "Você escolheu X!"
        elif usuario_input == 'O':
            return "Você escolheu O!"
        else:
            print("Valor inválido, por favor insira a forma correta!")  # Mensagem de erro
    
print(add_X_or_O())



