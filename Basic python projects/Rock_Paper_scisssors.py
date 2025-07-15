import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter an option(rock,paper,scissors):").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("its a tie")

    elif player == "rock" and computer == "scissors":
        print("The player has won")

    elif player == "paper" and computer == "rock":
        print("Player has won ")

    elif player == "scissors" and computer == "paper":
        print("The player has won ")

    else:
        print("Player has lost")
    if not input("Play again (y/n):").lower() == "y":
        playing = False
print("Thanks for playing")
