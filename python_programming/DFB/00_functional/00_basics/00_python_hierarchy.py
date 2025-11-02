# Implicit multiline statement
# a = [1,2,3,4,5]
# print(a)
a = [1,2,3 #comment here
     ,4,5]
print(a)

b = (1,2,3,4,5)
print(b)

b1 = (1,2 # comment here
          ,3,4,5)
print(b1)

a = {'key1':'value1','key2':'value2'}
print(a)

a1 = {'key1':'value1' # comment here
    ,'key2':'value2'
      # comment here
    }
print(a1)


def my_func(a, # this is used to indicate
            b, # this is also for
            c # this is for)
            ):
    print(a, b, c)

my_func(1,2,3)


# Explicit

a = 10
b = 20
c = 30

if a > 5 and b > 10 and c > 20:
    print('yes')

if a > 5 \
    and b > 10 \
    and c > 20:
    print('yes')

# Multiline string
a = '''This is a string'''
print(a)
a1 = '''This is 
a string'''
print(a1)


def my_func():
    a  = '''a multiline string
that is indented in the second line'''
    return a

print(my_func())