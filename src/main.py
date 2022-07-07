import help


def reprint_gameboard(X_coors, O_coors):
    """Redraws the game board in the console"""
    # goes through all the rows and columns and adds the things
    for i in range(9):
        row = i // 3
        column = i % 3

        if i % 3 == 0:
            if i != 0:
                print("|", end="")
                print()
            print("-------------")

        print("|", end="")

        if (column, row) in X_coors:
            print(" X ", end="")
        elif (column, row) in O_coors:
            print(" O ", end="")
        else:
            print("   ", end="")

    print("|", end="")
    print()
    print("-------------")


def strip_all_elements(list_):
    for i, string_ in enumerate(list_):
        list_[i] = string_.strip()
    return list_

def convert_all_elements_to_ints(list_):
    for i, element in enumerate(list_):
        list_[i] = int(element)
    return list_


def check_and_convert_input(user_input):
    """Applys strip_all_elements and convert_all_elements_to_ints on a list and returns it as a list.
    If the input isn't in the correct Format or the coordinates are out of range
    , it returns None. It also checks if the user wants to reset or exit the game or if the player 
    wants to see the help text."""

    match(user_input.lower()):
        case "exit":        
            print("'Til next time!")
            exit()
        case "reset":
            print("Resetting game")
            return "reset"
        case "help":
            print(help.help_text)
            return "help"

    user_input = user_input.split(",")
    if len(user_input) != 2:
        return None
    try:
        user_input = convert_all_elements_to_ints(strip_all_elements(user_input))
    except ValueError:
        return None
    else:
        user_input[0] -= 1
        user_input[1] = -(user_input[1] - 1) + 2
        if None in user_input:
            return None
    return tuple(user_input)


def win_draw_check(X_coors, O_coors):
    if len(X_coors + O_coors) >= 9:
        return "draw"
    # 3 in a row
    won = False
    for player in X_coors, O_coors:
        for row in range(3):
            won = True
            for column in range(3):
                if (column, row) not in player:
                    won = False
            if won == True:
                return player
    # 3 in a column
    won = False
    for player in X_coors, O_coors:
        for column in range(3):
            won = True
            for row in range(3):
                if (column, row) not in player:
                    won = False
            if won == True:
                return player
    # diagonal
    for player in X_coors, O_coors:
        for inverter in range(2):
            won = True
            for i in range(3):
                # y coor is inverted for bottom left -> top right
                if (i, i + (-2 * i + 2) * inverter) not in player:
                    won = False
            if won == True:
                return player
    
    return None
    
            



def main():
    print("xxxTIC TAC TOExxx")

    counter = -1     # keeps track of whos turn it is
    X_coors = []
    O_coors = []
    user_input = 0

    while True:
        if user_input  is not None:
            reprint_gameboard(X_coors, O_coors)
            counter *= -1
            won = win_draw_check(X_coors, O_coors)
            if won == "draw":
                print("Draw!")
                while True:
                    if (response := input("Do you want to play again? (Y/N) ").lower()) == "y":
                        X_coors.clear()
                        O_coors.clear()
                        break
                    elif response == "n":
                        exit()
                continue
            elif won is X_coors:
                print("Player X won!")
                while True:
                    if (response := input("Do you want to play again? (Y/N) ").lower()) == "y":
                        X_coors.clear()
                        O_coors.clear()
                        break
                    elif response == "n":
                        exit()
                continue
            elif won is O_coors:
                print("Player O won!")
                while True:
                    if (response := input("Do you want to play again? (Y/N) ").lower()) == "y":
                        X_coors.clear()
                        O_coors.clear()
                        break
                    elif response == "n":
                        exit()
                continue
                    
        if user_input is None:
            user_input = check_and_convert_input(input())
        else:
            player = "X" if counter == 1 else "O"
            print(f"{player}-Player:") 
            user_input = check_and_convert_input(input(f"Please enter the position of your next {player} (x_coor, y_coor). For further information type help!\n"))

        if user_input is None:
            print("Please enter your coordinates in a valid format!")
            continue
        
        if user_input in X_coors or user_input in O_coors:
            print("Cell occupied!")
            user_input = None
            continue

        if user_input == "reset":
            X_coors.clear()
            O_coors.clear()
            continue
        
        if user_input == "help":
            user_input = None
            continue


        X_coors.append(tuple(user_input)) if counter == 1 else O_coors.append(tuple(user_input))
3
        
if __name__ == "__main__":
    main()
