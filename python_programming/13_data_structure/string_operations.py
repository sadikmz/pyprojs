#  Concatenate
str1 = "Hello"
str2 = "World"

print(str2 +" "+ str2)

# using "in" operator - logical

print("t" in str1)

# Alphabetical order

new_string = input("Enter a string")

if new_string < "test":
    print(f"{new_string} comes before test" )
elif new_string > "test":
    print(f"{new_string} comes after test")
else:
    print(f"{new_string} and hello start with same letter")