# score = float(input("Enter score: "))

try:
    score = float(input("Enter score: "))
except ValueError:
    print("Bad score")
    quit()

if score <0.0 or score > 1.0:
    print("Bad score")
    quit()
elif score >0.9:
    print("Your grade is B")
elif score <0.9 and score >= 0.8:
    print("Your grade is B")
elif score < 0.7 and score >= 0.6:
    print("Your grade is C")
elif score < 0.6 and score >= 0.5:
    print("Your grade is D")
else:
    print("Your grade is F")