import argparse
import datetime

parser = argparse.ArgumentParser(description='Returns a string containing the name and age of a person')
parser.add_argument('-f', '--first', type=str, help='Specify the first', required=False, dest='first_name')
parser.add_argument('-l', '--last', type=str, help='Specify the last ', required=True, dest='last_name')
parser.add_argument( '-y', type=int, help='year of birth', required=True, dest='birth_year')

args = parser.parse_args()

print(args)

if args.first_name:
    names = [args.first_name]
else:
    names = []

names.append(args.last_name)
full_name = ' '.join(names)

current_year = datetime.datetime.utcnow().year
age = current_year - args.birth_year

print(f'{full_name} is {age} years old.')

