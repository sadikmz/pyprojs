# run.py

# print(f'loading run.py: __main__= {__name__}')

# import module1

import timing

code = '[x**2 for x in range(1_000)]'

print(code)

result = timing.timeit(code, 100)
print(result)

# print(dir(timing))