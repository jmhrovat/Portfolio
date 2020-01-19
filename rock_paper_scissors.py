import random

print("Welcome to Rock, Paper, Scissors")

playing = True
choices = ["rock", "paper", "scissors"]

while playing:
    cpu_choice = random.choice(choices)
    player_choice = raw_input()

    if cpu_choice == player_choice:
        print("It's a tie")
    elif cpu_choice == "rock":
        if player_choice == "scissors":
            print("You lost")
        else:
            print("You won!")
    elif cpu_choice == "scissors":
        if player_choice == "paper":
            print("You lost")
        else:
            print("You won!")
    elif cpu_choice == "paper":
        if player_choice == "rock":
            print("You lost")
        else:
            print("You won!")
    else:
        print("Invalid input")

    print("Keep playing? Type 'n' to quit")
    answer = raw_input()
    if answer == "n":
        playing = False
    else:
        cpu_choice = None
        player_choice = None


# rock_paper_scissors.py
