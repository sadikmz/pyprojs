import random
import math

lower_bound = int(input("Enter Lower bound: "))
upper_bound = int(input("Enter Upper bound: "))

number_of_chances = int(math.log(upper_bound-lower_bound+1,2))
guess_correct = random.randint(lower_bound, upper_bound)
print(f"\n\tYou have only {number_of_chances} chances to guess the integer!\n")

counter = 0
# while counter < number_of_chances:
#     guess = int(input("Guess a number: "))
#     counter +=1
#     if guess_correct < guess:
#         print("You guessed too high!")
#     elif guess_correct > guess:
#         print("You guessed too low!")
#     elif guess_correct == guess:
#         print(f"Congratulations you did guess it in {counter} try!")
#         print(f"The number is {guess}")
# guess = 0
while counter < number_of_chances:
    guess = int(input("Guess a number: "))
    counter +=1
    if guess_correct == guess:
        print(f"Congratulations you did guess it in {counter} try!")
        break
    elif guess_correct < guess:
        print("You guessed too high!")
    elif guess_correct > guess:
        print("You guessed too low!")
print(f"The number is {guess_correct}")
print(f"\tBetter Luck Next Time")