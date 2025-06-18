year = int(input("Enter year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("This is not Leap Year")
    else:
        print("This is not a Leap Year")
else:
    print("Not a leap year")
