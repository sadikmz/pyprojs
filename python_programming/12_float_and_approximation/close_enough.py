#  Recall the approximation method code to find
x = 54321
epsilon = 1
num_guesses = 0
guess = 0.0
increment = 0.0001
while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
if abs(guess**2 - x) >= epsilon:
    print(f'Failed on square root of {x}')
    print(f'Last guess was {guess}')
    print(f'Last guess squared {guess**2}')
else:
    print(f'{guess} is close enough to  {x}')