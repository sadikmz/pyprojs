try:
    hour = int(input("Enter hour: "))
except ValueError:
    print("Error, please enter a number input for hour")
    quit()

try:
    rate = int(input("Enter rate: "))
except ValueError:
    print("Error, please enter a number input for rate")
    quit()

if hour < 40:
    pay = round(hour * rate, 2)
else:
    overtime = hour - 40
    pay = round(40*rate + overtime*rate*1.5, 2)
print(f"Pay {pay}")


#  print ValueError
# print()

# quit()