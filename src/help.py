help_text = """\
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
- inputting reset will reset the game"""