""" ROCK PAPER SCISSOR GAME """

"""Workflow of Project : 

1. Input from user (Rock , Paper Scissor)
2. Computer choice (computer will choose randomly not conditionally )
3. Print result 

Cases:
A - Rock 
Rock - Rock : tie 
rock - scissor :rock win 
rock - paper  : paper win 

B - Scissor 
Scissor - rock : rock win 
scissor - paper : scissor win 
scissor - scissor : tie 

C - Paper 
paper - rock : paper win 
paper - scissor : scissor win 
paper - paper : tie 

"""

print("LETS PLAY ROCK - PAPER - SCISSOR :) , \n")

import random 

choices = ["rock","paper" , "scissor"]

User_input = input("Enter your move (Rock / Paper / Scissor) : ").strip().lower()
Computer_input = random.choice(choices).strip().lower()

# print("Your move :" , User_input)
# print("Computer's move : " , Computer_input)
#   or 
print(f"Your move = {User_input}, Computer's move = {Computer_input}")

if(User_input == Computer_input):
    print("Both choosed same move ")
    print("Tie !!")

elif(User_input == "rock"):
    if(Computer_input == "scissor"):
        print("You Win !")

    else:
        print("You Lose !")

elif(User_input == "paper"):
    if(Computer_input == "scissor"):
        print("You Lose ! ")

    else:
        print("You Win !")

elif(User_input == "scissor"):
    if(Computer_input == "rock"):
        print("You lose ! ")

    else:
        print("You Win !")

