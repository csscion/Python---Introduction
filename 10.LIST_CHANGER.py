from IPython.display import clear_output

def display_game_list(game_list):
    print(game_list)

def position_to_change():
    while True:
        try:
            choice = int(input("Enter the number of position that you want to change (0, 1, 2): "))
            if choice not in range(0, 3):
                clear_output()
                print("INCORRECT INPUT. PLEASE SELECT BETWEEN (0, 1, 2):")
                continue
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter an integer.")
        return False

def replacement_word(game_list, choice):
    
    while True:
        user_placement = input("Type a string to place at the position: ")
        game_list[choice] = user_placement
        print(game_list)
        return False
        

def gameon_choice():
    choice="wrong"
    while True:
        try:
            choice = input("Would you like to keep playing? Y or N ")
            if choice not in ['Y', 'N']:
                clear_output()
                print("Sorry, I didn't understand. Please make sure to choose Y or N.")
                continue
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter an integer.")
        if choice == "Y":
        # Game is still on
            return True
        else:
        # Game is over
            return False


game_on = True
game_list = ['hi', 'no', 2]

while game_on:
    clear_output()
    display_game_list(game_list)
    choice = position_to_change()
    replacement_word(game_list, choice)
    clear_output()
    display_game_list(game_list)
    game_on = gameon_choice()
