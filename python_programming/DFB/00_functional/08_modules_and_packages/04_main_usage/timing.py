# timing.py

# print("Loading timing")

"""
Times how long a snippet of code takes to run
over multiple iteration. 
"""

from time import perf_counter
from collections import namedtuple
import argparse

Timing = namedtuple('Timing', 'repeats elapsed average')

def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average)

if __name__ == '__main__':
    # Get code, repeats from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code', type=str, help= 'This Python code snippet to time')
    parser.add_argument('-r', "--repeats",
                        type=int,
                        help= 'Number of times to run the code')
    args = parser.parse_args()
    # print(args.code)
    # print(args.repeats)
    # print('Running this commandline code')
    print(f'timing: {args.code}')
    print(timeit(code=str(args.code), repeats=args.repeats))