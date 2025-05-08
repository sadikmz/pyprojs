your_age = input("How old are you?: ")
# print("Your are", your_age, "years old!")

your_age = int(your_age)

if your_age > 18:
    print("You are officially allowed to vote and buy groceries.")
else:
    print("Dear customer, we are really sorry that you're not allowed to vote and buy groceries due to age limit restriction imposed by the local government.")