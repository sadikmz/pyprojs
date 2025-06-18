student_scores = [80,60,50,65,75,55]

highest = 0

for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score in the class is {highest}")