# Write a programme where the computer randomly generates a number between 0 and 20. 
# The user needs to guess what the number is. 
# If the user guesses wrong, tell them their guess is either too high, or too low. 


import random

print("Welcome to guess the number")
value = random.randrange(1, 20)

print("Guess the number")
player_won = False
while player_won is not True:
    guess = input()
    if guess < value:
        print("Too low, try again")
    elif guess > value:
        print("Too high, try again")
    else:
        print("Correct!")
        player_won = True

