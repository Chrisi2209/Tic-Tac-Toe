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

reprint_gameboard([(0, 0), (1, 1), (0, 2)], [(0, 1), (2, 0), (2, 2)])
