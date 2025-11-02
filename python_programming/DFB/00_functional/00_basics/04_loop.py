a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
if not found:
    l.append(val)



print(l)
print(l)


l = [1, 2, 3,10]
val = 11
idx = 0

while idx < len(l):
    if l[idx] == val:
        # found = True
        break
    idx += 1
else:
    l.append(val)

    print(l)

# try...except...finally

a = 10
b = 0

try:
    a / b
except ZeroDivisionError:
    print("division by zero")
finally:
    print("This always executes")



a = 0
b = 10

while a < 4:
    print("............................")
    a += 1
    b -= 1
    try:
        a / b
    except ZeroDivisionError:
        print("{0}, {1} - division by zero".format(a, b))
        break
    finally:
        print("{0}, {1} - always executes".format(a, b))

    print("{0}, {1} - main loop".format(a, b))
else:
    print('Code executed without zero division')



for i in range(1,5):
    print(i)
    if i % 7 == 0:
        print("Multiple of 7 found")
        break
else:
    print("No multiple of 7 found")