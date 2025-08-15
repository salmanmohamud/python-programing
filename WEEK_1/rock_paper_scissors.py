# Build a Human-versus-Computer Rock-Paper-Scissors Game
# In this project, you will create a script to allow the user to play rock-paper-scissors against the computer. For starters, if you are not familiar with the game, you need to understand that: rock beats scissors, scissors beats paper, and paper beats rock. Here are the steps to follow in build your game:

# Utilise the Random Python Library to allow the computer to randomly choose rock, paper, or scissors in each round
# Allow the user to now input their choice and compare it directly with the computer’s choice. You can then declare the winner of the round based on the rules of the game
# Now, instead of declaring the winner, just assign a point to the winner of a round. This should allow you to utilise loops to increase the rounds within a game to 3 or 5. Your program will assign points to the winner of each round and declare the winner after all rounds i.e the one with the most points.
# To make the game more efficient, stop the game and declare the winner immediately a user guess 2 points out of 3 in a 3-round game or 3 out of 5 points in a 5-round game. This should stop the game from continuing when there’s already a clear winner even if all rounds have not been completed.
# You can now freely play rock-paper-scissors with your computer and see how well you perform against the computer’s randomised choices.

import random
user_wins=0
comp_wins=0
for i in range(3):
    user_choice = input ("choose ")
    Random_Number = random.randint(0,2)

    choices = ["rock", "paper","scissor"]
    # choices[2]
    # print (choices[2])
    computer_choice =choices[Random_Number]
    print (computer_choice)

    if user_choice == "rock" and computer_choice == "paper":
        print("You Lost")
        comp_wins= comp_wins+1 
    elif user_choice == "paper" and computer_choice == "scissor":
        print("You Lost")
        comp_wins= comp_wins+1 
    elif user_choice == "scissor" and computer_choice == "rock":
        print("You Lost looser")
        comp_wins= comp_wins+1 
    elif user_choice == computer_choice:
        print("Its a Draw")

    else :
        print("YOU WIN!!!!")
        user_wins= user_wins+1

    if user_wins > 1:
        print("WINNER")
        break
    elif comp_wins > 1:
        print("LOOSER")
        break
if user_wins > comp_wins:
    print("WINNER")
elif comp_wins > user_wins:
    print("LOOSER")
