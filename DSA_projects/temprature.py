def temprature(n):
    if n < 18:
        return "Cold"
    elif 18 <= n <= 28:
        return "Warm"
    else:
        return "Hot"

temp = int(input("Enter temperature: "))
print(temprature(temp))
