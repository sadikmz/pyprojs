# Example of the sqrt function in Python's math library perform error-checking that might be implemented as follows:
def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x cannot be negative")
    # Do the real work here