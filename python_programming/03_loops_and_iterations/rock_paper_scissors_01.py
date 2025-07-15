
import random
def select_computer_action():
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    return computer_action

def determine_winner(p_computer_action, p_user_action):
    if p_user_action == p_computer_action:
        print(f"Both players selected {p_user_action}. It's a tie!")
    elif p_user_action =="rock":
        if computer_action == "scissors":
            print("Rock smashed scissors. You win!")
        else:
            print("Paper covers rock! You lose.")
    elif p_user_action == "paper":
        if computer_action == "scissors":
            print("Scissors cut paper. You lose.")
        else:
            print("Paper covers rock! You win!")
    elif p_user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")



while True:
    user_action = input("Enter a choice (rock, paper, scissors): ")
    # possible_actions = ["rock","paper","scissors"]
    computer_action = select_computer_action()
    print(f"\nYou chose {user_action}, computer chose {computer_action}")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action =="rock":
        if computer_action == "scissors":
            print("Rock smashed scissors. You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "scissors":
            print("Scissors cut paper. You lose.")
        else:
            print("Paper covers rock! You win!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cut paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")
    play_again = input("Play again (Y/N)? ")
    if play_again != "Y":
        break


select_computer_action()