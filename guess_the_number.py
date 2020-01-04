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
# python guess_the_number.py
