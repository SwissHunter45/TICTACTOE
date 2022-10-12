import random

board = """     
     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
 """
a = list(board)
mylist = []
game_count = 0
j = True

while j == True:
    user_input = input(":")
    mylist.append(user_input)
    game_count += 1 
    if user_input == "1":
        board[26] = "X"
        print(board)




