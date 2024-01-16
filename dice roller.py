#dice game
import random
import time

"""
Rules
1) 2 players
2) roll 2 d6's
3) if sum is a multiple of 5, +10 points
4) if doubles, roll again
5) if sum is odd, -5 points
"""

#score setup
player_1 = 0
player_2 = 0
winner_score = 0

#authentication/login
def authentication():
    user_p1 = "p1"
    pass_p1 = "p1"
    user_p2 = "p2"
    pass_p2 = "p2"

    p1_us = input("Player 1: Username: ")
    p1_pa = input("Player 1: Password: ")

    if p1_us != user_p1 or p1_pa != pass_p1:
        print("Incorrect")
        input()

    else:
        print("Correct")

    p2_us = input("Player 2: Username: ")
    p2_pa = input("Player 2: Password: ")

    if p2_us != user_p2 or p2_pa != pass_p2:
        print("Incorrect")
        input()

    else:
        print("Correct")

#player 1 game
def player1():
    global player_1
    p1_num1 = random.randint(1,6)
    p1_num2 = random.randint(1,6)
    p1_total = 0
    print(p1_num1)
    print(p1_num2)
    
    p1_num3 = 0
    if p1_num1 == p1_num2:
        print("Doubles: Roll again")
        p1_num3 = random.randint(1,6)
        print(p1_num3)
        p1_total = p1_total + p1_num3

    p1_total = p1_num1 + p1_num2
    if p1_total % 5 == 0:
        player_1 = player_1 + 10
        print("Multiple of 5: +10 points")

    if p1_total % 2 != 0:
        print("Odd: -5 points")
        player_1 = player_1 - 5
        if player_1 < 0:
            player_1 = 0

    player_1 = p1_total + player_1
    time.sleep(1)
    print("Player 1 total:", player_1, "\n")

#player 2 game
def player2():
    global player_2
    p2_num1 = random.randint(1,6)
    p2_num2 = random.randint(1,6)
    p2_total = 0
    print(p2_num1)
    print(p2_num2)

    p2_num3 = 0
    if p2_num1 == p2_num2:
        print("Doubles: Roll again")
        p2_num3 = random.randint(1,6)
        print(p2_num3)
        p2_total = p2_total + p2_num3

    p2_total = p2_num1 + p2_num2
    if p2_total % 5 == 0:
        player_2 = player_2 + 10
        print("Multiple of 5: +10 points")

    if p2_total % 2 != 0:
        print("Odd: -5 points")
        player_2 = player_2 - 5
        if player_2 < 0:
            player_2 = 0


    player_2 = p2_total + player_2
    print("Player 2 total:", player_2, "\n")

#gameplay
count = 0
authentication()
while count <= 5:
    print("Player 1")
    p1_r = input("Press R and/or enter to roll ")
    player1()
    print("Player 2")
    p2_r = input("Press R and/or enter to roll ")
    player2()
    count = count + 1

#player 1 win
if player_1 > player_2:
    print("Player 1 Wins!!")
    print("Player 1:", player_1)
    print("Player 2:", player_2)
    winner_score = player_1

#player 2 win
elif player_2 > player_1:
    print("Player 2 Wins!!")
    print("Player 1:", player_1)
    print("Player 2:", player_2)
    winner_score = player_2

#draw
elif player_1 == player_2:
    print("Draw")
    tiebreak = input("Press R or enter to find the winner ")
    p1_tr = random.randint(1,6)
    p2_tr = random.randint(1,6)

    while True:
        if p1_tr == p2_tr:
            p1_tr == random.randint(1,6)
            p2_tr == random.randint(1,6)
        else:
            break

    print("Player 1 rolled:", p1_tr)
    print("Player 2 rolled:", p2_tr)

#scoreboard input
name = input("Name? ")
name = name + " "
winner_score = str(winner_score)
with open("scores.txt", "a") as scores: 
    scores.write("\n")
    scores.write(name)
    scores.write(winner_score)
    scores.write("\n")
    scores.close
    
