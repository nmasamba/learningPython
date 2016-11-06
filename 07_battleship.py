
"""

Author: Nyasha Pride Masamba

Based on the lessons from Codecademy at https://www.codecademy.com/learn/python

This Python program is a console implementation of the classic board game Battleship.
In this version of the game, there will be a single ship hidden in a random location 
on a 5x5 grid. The player will have 10 guesses to try to sink the ship. Prior knowledge
of Python lists, conditionals and functions come together to create the game (along
with loops, which will be covered in more detail in the next few posts). Suggestions
for enhancement of the program include:
- Make multiple battleships
- Make your game a two-player game
- Use functions to allow your game to have more features like rematches, statistics and more!

Example input:
                                                                                                                                                    
Turn 1                                                                                                                                                          
Guess Row:2                                                                                                                                                     
Guess Col:3                                                                                                                                                     
                                                                                                                                                                                                                                                                                                  
Turn 2                                                                                                                                                          
Guess Row:3                                                                                                                                                     
Guess Col:3                                                                                                                                                    

Example output:
Let's play Battleship!                                                                                                                                          
O O O O O                                                                                                                                                       
O O O O O                                                                                                                                                       
O O O O O                                                                                                                                                       
O O O O O                                                                                                                                                       
O O O O O                                                                                                                                                       
Turn 1                                                                                                                                                          
Guess Row:2                                                                                                                                                     
Guess Col:3                                                                                                                                                     
You missed my battleship!                                                                                                                                       
1                                                                                                                                                               
Turn 2                                                                                                                                                          
Guess Row:3                                                                                                                                                     
Guess Col:3                                                                                                                                                     
Congratulations! You sunk my battleship! 

"""



from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!


for turn in range(4):
    print "Turn", turn + 1
    
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
            turn = turn + 1
            print turn
    
    if turn==4:
        print"Game Over"
        print_board(board)
        
        