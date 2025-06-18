hour = float(input("Enter hour: "))
rate = float(input("Enter rate: "))

if hour < 40:
    pay = round(hour * rate, 2)
else:
     overtime = hour - 40
     pay = round(40*rate + overtime*rate*1.5, 2)
print(f"Pay {pay}")