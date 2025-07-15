
import random

while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock","paper","scissors"]
    compute_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {compute_action}")

    if user_action == compute_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action =="rock":
        if compute_action == "scissors":
            print("Rock smashed scissors. You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if compute_action == "scissors":
            print("Scissors cut paper. You lose.")
        else:
            print("Paper covers rock! You win!")
    elif user_action == "scissors":
        if compute_action == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    play_again = input("Play again (Y/N)? ")
    if play_again != "Y":
        break
