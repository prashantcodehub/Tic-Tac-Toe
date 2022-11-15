#                  !!!!!!!        _*_|_ _|_*_
# tic tac toe game \* ! */        _ _|_ _|_ _
#                   \ ~ /            | O |
#                    \_/
import os
import random
from time import sleep

G_m = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def Check_Winner(i):
    if G_m[i] == 'O':
        print('Player 1 ')
        print(''' 
            *`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*
              *  \\  //\\  //  ||   ||\\ ||   *
              *   \\//  \\//   ||   || \\||   *
            *`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*
    ''')
    else:
        print('Player 2 ')
        print(''' 
            *`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*
              *  \\  //\\  //  ||   ||\\ ||   *
              *   \\//  \\//   ||   || \\||   *
            *`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*`*
    ''')
    return 1


def check_conditions():
    if G_m[0] == G_m[1] == G_m[2]:
        Check_Winner(1)

    if G_m[3] == G_m[4] == G_m[5]:
        Check_Winner(4)

    if G_m[6] == G_m[7] == G_m[8]:
        Check_Winner(7)

    if G_m[0] == G_m[3] == G_m[6]:
        Check_Winner(3)

    if G_m[1] == G_m[4] == G_m[7]:
        Check_Winner(4)

    if G_m[2] == G_m[5] == G_m[8]:
        Check_Winner(5)

    if G_m[0] == G_m[4] == G_m[8]:
        Check_Winner(4)

    if G_m[2] == G_m[4] == G_m[6]:
        Check_Winner(4)


for i in range(0, 9):
    print("""welcome to 
                                 !!!!!!!        _ _|_ _|_ _
                tic tac toe      \* ! */        _ _|_ _|_ _
                                  \ ~ /            |   |
                                   \_/
                                            _(0)_|_(1)_|_(2)_      | Positions |
                                            _(3)_|_(4)_|_(5)_      
                                             (6) | (7) | (8)
                                             
            It is a 2 player game " PLAYER1 -> O   v/s   PLAYER2 -> X  "
            first to get 3    'O' or 'X'  in a row, colomn or diagnol wins
        ......................................................................

    """)

#    tos = random.randrange(1, 3)
#    if tos == 1:
#        print('Player 1 gets the first chance')
#    else:
#        print('Player 2 gets the first chance')

    x = f"                  _{G_m[0]}_|_{G_m[1]}_|_{G_m[2]}_"
    y = f"                  _{G_m[3]}_|_{G_m[4]}_|_{G_m[5]}_"
    z = f"                   {G_m[6]} | {G_m[7]} | {G_m[8]} "
    print(x)
    print(y)
    print(z)

    location = int(input())

    if i % 2 == 0:
        G_m[location] = 'O'
    else:
        G_m[location] = 'X'

    if i >= 5:
        win_flaf = check_conditions()
        if win_flaf == 1:
            break
