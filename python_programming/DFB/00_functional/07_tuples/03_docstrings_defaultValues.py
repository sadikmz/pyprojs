from collections import namedtuple

Stock = namedtuple('Stock', '''symbol 
year 
month 
day 
open 
high 
low 
close''')

StockExt = namedtuple('StockExt', Stock._fields + ('previouse_close',))

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)


Stock.__doc__ = "Representation of 2D Cartesian coordinates"
Stock.symbol.__doc__ = "Symble of the stock market"
Stock.year.__doc__ = "Year of the stock"
print(Stock.__doc__)
print(Stock.year.__doc__)
print(Stock.symbol.__doc__)

# Default values: using a  Prototype

Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x, origin_y')
vector_zero = Vector2D(x1 = 0, y1 = 0, x2 = 0, y2 = 0, origin_x = 0, origin_y = 0)
vector_zero = Vector2D(0,0,0,0,0,0)
print(vector_zero.__doc__)
# vector_one = Vector2D(1, 0)

# to modify vector_zero use _replace but it create a new vector

new_vec = vector_zero._replace(x1=10,y1=20)
print(new_vec)
print(id(new_vec))
print(id(vector_zero))

# Using __default__

Vector2D.__new__.__defaults__ = (8,10,10)
# vector_zero = Vector2D(x1=0, y1=0, x2 = 0, y2 = 0, origin_x = 0, origin_y = 0)
vector_zero = Vector2D(0, 0,0)
print(vector_zero)
# print(Vector2D.__name__.__defaults__)