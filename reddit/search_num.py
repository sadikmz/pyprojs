target = input("Enter number to search for: ")
count = 0
found = False
while found == False:
    for i range(10):
        if numbers[count] == target:
            print("The number is in the list")
            found = True
        else:
            count += 1
            if count == 11:
                print("The number is not in the list")
                found = True

