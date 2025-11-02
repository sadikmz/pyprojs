class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        print(f'You called a + on {self} and {other}')
        return 'Hello from __add__'

    def __iadd__(self, other):
        print(f'You called i += on {self} and {other}')
        return 'Hello from __iadd__'


c1 = MyClass('instance 1')
c2 = MyClass('instance 2')
print(id(c1))
result = c1 + c2
# print(result)

# print(c1,c2)
print(c1)
print(id(c1))
c1 += c2
print(id(c1))
print(c1)

# add actual concatenation and in-place concatenation to MyClass

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        # print(f'You called a + on {self} and {other}')
        return MyClass(self.name + other.name)
        # return 'Hello from __add__'

    def __iadd__(self, other):
        if isinstance(other,MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

c1 = MyClass('Eric')
c2 = MyClass('Idel')
print(id(c1))
print(id(c2))

result = c1 + c2
print(c1)
print(id(c1))

c1 += c2
print(c1)
print(id(c1))

# Implement repetition
class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        # print(f'You called a + on {self} and {other}')
        return MyClass(self.name + other.name)
        # return 'Hello from __add__'

    def __iadd__(self, other):
        if isinstance(other,MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __imul__(self, n):
        self.name *= n
        return self


c1 = MyClass('Eric')
print(c1)
result = c1 * 3
print(id(result))
print(result)
print(id(c1))
c1 *= 10
print(id(c1))
print(c1)

# Supporting int * string (or other type of object): implement __rmul__

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        # print(f'You called a + on {self} and {other}')
        return MyClass(self.name + other.name)
        # return 'Hello from __add__'

    def __iadd__(self, other):
        if isinstance(other,MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __imul__(self, n):
        self.name *= n
        return self


c1 = MyClass('Eric')
print(c1*3)
print(3*c1)

# Using in Operator

l = [1,2,3,4]
s = 'python'

print(1 in l)
print('a' in s)

# implementing __contain__ method

class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass (name = {self.name})'

    def __add__(self, other):
        # print(f'You called a + on {self} and {other}')
        return MyClass(self.name + other.name)
        # return 'Hello from __add__'

    def __iadd__(self, other):
        if isinstance(other,MyClass):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __imul__(self, n):
        self.name *= n
        return self

    def __contains__(self, value):
        return value in self.name


c1 = MyClass('Eric Idel')
print('Eric' in c1)
print('Z' in c1)

