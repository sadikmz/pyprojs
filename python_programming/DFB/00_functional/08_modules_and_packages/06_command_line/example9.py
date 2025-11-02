import argparse

parser = argparse.ArgumentParser(description='Testing defaults and flags')

# parser.add_argument('--monty', action='store_const', const='Python')
# parser.add_argument('--n', '--name',  action='store', default='John')
# parser.add_argument('-v', '--verbose', action='store_const', default=False, const=True)
# parser.add_argument('-v2', action='store_const', const=True)
# parser.add_argument('-q', '--quite', action='store_false')
parser.add_argument('-q', '--quite', action='store_true')
parser.add_argument('-q2', action='store_const', const=False, default=False)

args = parser.parse_args()

print(args)