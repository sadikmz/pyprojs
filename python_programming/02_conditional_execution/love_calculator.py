name1 = input("What is your name? ")
name2 = input("What is your name? ")

# score
name3 = name1 + name2
name3 = name3.lower()
letters = "TRUELOVE"
letters = letters.lower()

score = 0

for letter in letters:
    score +=name3.count(letter)
    
if score < 10 or score > 85:
    print(f"Your score is {score}, and you go together like coke and mentos.")
elif score >=40 and score <=70:
    print(f"Your score is {score}, and you are alright togather.")
else:
    print(f"Your score is {score}.")
