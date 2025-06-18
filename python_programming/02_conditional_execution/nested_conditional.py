# height = float(input("Enter your height in m: "))
# weight =  float(input("Enter your weight in kg: "))
# # TODO
# BMI = round(weight/(height**2),2)
# # print("Your BMI is:", BMI)



# if BMI < 18.5:
#     print("Your BMI are underweight")
# elif 18.5 <= BMI < 25

# :
#     print("Your BMI are normal")
# elif 25 <= BMI < 30:
#     print("Your BMI are overweight")
# elif 30 <= BMI < 35:
#     print("Your BMI are obese")


# TODO
# TODO

print("Welcome to Burger Shop!")

size = input("What size burger do you want? M, N, or L ")
add_mushroom = input("Do you want mashroom? Y or N")
extra_cheese = input("Do you want extra cheese? Y or N")

bill = 0

if size == "M":
    bill += 5
elif size == "N":
    bill += 8
else:
    bill += 10


if add_mushroom == "Y":
    if size == "L":
        bill += 2
    else:
        bill += 1

if extra_cheese == "Y":
    bill += 1

print("Your final bill is: $" + str(bill))
