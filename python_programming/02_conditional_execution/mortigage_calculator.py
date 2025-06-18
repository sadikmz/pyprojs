print("Welcome to the Mortigage Calculator!")
salary = int(input("What is your salary? "))

rate = 0

if salary >= 2000:
    print("You are eligible for mortigage!")
    credit_score = int(input("What is your credit score? "))
    if credit_score >= 900 and credit_score <= 1000:
        rate = 3
        print("Your credit score is: 3%")
    elif credit_score > 800:
        rate = 4
        print("Interest rate is: 4%")
    elif credit_score >750:
        rate = 6
        print("Interest rate is: 6%")
    else:
        rate = 8
        print("Interest rate is: 8%")
    disability = input("Do you have any disability? Y or N.")
    if disability == "Y":
        rate -=2
    print(f"Your final rate is ${rate}%")
else:
    print("Sorry, your are not eligible for mortigage.")

