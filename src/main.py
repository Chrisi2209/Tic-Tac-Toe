from mailbox import FormatError


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
            print("""\
Help text:
----- rules 
- there are two players
- the two players alternately draw their symbol (X or O) into an unoccupoed the field on the board (X goes first)
- the first player to have 3 of their own symbol in a row wins the game
- if the board is filled and no player won, the game is a draw

----- formatting and allowed values of inputs
- every turn, you have to specify the x and y coordinates of your placement.
- the coordinate grid is layed out so that the bottom left cell is (1|1)
- both coordinates have to be in a range from 1 to 3
- the specified cell is not allowed to already be occupied

----- special functions
- inputting exit will exit the game
- inputting reset will reset the game\
""")
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

        elif user_input == "reset":
            X_coors.clear()
            O_coors.clear()
            continue
        
        if user_input == "help":
            user_input = None


        X_coors.append(tuple(user_input)) if counter == 1 else O_coors.append(tuple(user_input))
        print(X_coors)


        
if __name__ == "__main__":
    main()
