# years = input("Enter number of years ")
# # totYears = int(years)
# weeks = 52*int(years)
# # totWeeks = str(weeks)
# print("There are " +str(weeks)+ " weeks in " +years+ " years" )
# print(f"There are {weeks} weeks in {years} years" )


# name=input("Enter your name ")
# print(f"Hello {name}.\nWelcome to the Python")
# print("Hello " +name+"\n" + "Welcome to the Python")

# print("Welcome to the Group name Generator")
# fav_color = input("What is your favourite color? ")
# print(fav_color)
# fav_animal = input("What is your favourite animal? ")
# print(fav_animal)
# # print(f"Your group name could be {fav_color} {fav_animal}")
# print("Your group name could be "+fav_color+" "+fav_animal+"s")

"""Gross pay"""

# hours = input("Enter hours: ")
# rate = input("Enter rate: ")
#
# print(f"Pay: {round(float(hours)*float(rate), 2)}")

""" Celsius to Fahrenheit """
# celsius = input("Enter temperature in Celsius: ")
# fahrenheit = (float(celsius) * 9 / 5) + 32
# print(f"{celsius} Celsius = {int(fahrenheit)} Fahrenheit")

""" Trip Cost Calculator"""

print("Welcome to the Trip Cost Calculator!")
days=input("How many days will you stay? ")
cost_per_day=input("How much does hotel cost per day? $")
flight_cost=input("How much does flight cost? $")
rental_car=input("If you need rental car please enter the price otherwise enter zero. $")
other_expenses=input("Enter other expenses? $")
tot_cost = float(cost_per_day) * float(days) + float(rental_car) * float(other_expenses)
tot_cost = round(tot_cost, 2)
print(f"The total: ${tot_cost}")