def reprint_gameboard(X_coors, O_coors):
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
        

def main():
    print("xxxTIC TAC TOExxx")

    counter = 0     # keeps track of whos turn it is
    X_coors = []
    O_coors = []

    reprint_gameboard(X_coors, O_coors)
    while True:
        counter += 1
        counter %= 2
        
        if counter == 1:
            print("X-Player:")
            X_coors.append(tuple(convert_all_elements_to_ints(strip_all_elements(input("Please enter the position of your next X (x_coor, y_coor):\n").split(",")))))

        else:
            print("Y-Player:")
            O_coors.append(tuple(convert_all_elements_to_ints(strip_all_elements(input("Please enter the position of your next O (x_coor, y_coor):\n").split(",")))))
        
        reprint_gameboard(X_coors, O_coors)

        
if __name__ == "__main__":
    main()
