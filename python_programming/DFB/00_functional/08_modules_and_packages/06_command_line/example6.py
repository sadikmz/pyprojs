import argparse
import sys

parser = argparse.ArgumentParser(description='This is calculates div  a//b and mod a%b of two integers')
parser.add_argument('a', help='first integer', type=int)
parser.add_argument('b', help='second integer', type=int)


# args = parser.parse_args(['100', '300'])
# args = parser.parse_args(sys.argv[1:])
args = parser.parse_args()

# print(args.a)
# print(args.b)

a = args.a
b = args.b

print(f'{a}//{b} = {a // b}, {a} % {b} = {a % b}')