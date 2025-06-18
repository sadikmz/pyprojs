def main():
    # Get a number from the user
    number = int(input("Please enter a number: "))
    
    # Check if the number is even or odd
    if is_even(number):
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
def is_even(num):
    # Check if the number is even
    return num % 2 == 0
