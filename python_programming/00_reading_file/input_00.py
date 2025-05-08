age = int(input("Enter your age in years: "))
max_heart_rate = 206.9 - (0.67*age)
target = 0.65*max_heart_rate
target = round(target,2)
print("Your target fat-burning heart rate is", target)