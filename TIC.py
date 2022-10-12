import random

mylist = []

v = True
j = True
game_count = 0

while j == True:
    user_input = int(input(""))
    mylist.append(user_input)
    game_count += 1
    print(mylist)

    while v == True:
        rng = random.randint(1,9)
        if rng not in mylist:
            mylist.append(rng)
            print(mylist)
            break
        else:
            v == False

        if game_count == 9:
            print("All nine indexes are filled out")
            j = False