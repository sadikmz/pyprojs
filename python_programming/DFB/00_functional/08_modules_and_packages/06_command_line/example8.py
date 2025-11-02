import argparse


parser = argparse.ArgumentParser(description='Print the squares of the list of numbers and the cubes of another list of numbers')
parser.add_argument('--sq', help='list of numbers to square', nargs="+", type=float)
parser.add_argument('--cu', help='list of numbers to cube', nargs="+", type=float, required=True, dest='cubes')

args = parser.parse_args()

if args.sq:
    squares = [n ** 2 for n in args.sq]
    print(f'{squares}')

cubes = [n ** 3 for n in args.cubes]
print(f'{cubes}')