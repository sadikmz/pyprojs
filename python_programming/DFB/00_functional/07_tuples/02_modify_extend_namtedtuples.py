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

djia_ext = StockExt(*djia, 26_000)
print(djia_ext)


djia_ext = StockExt._make(djia + (26_000,))
print(djia_ext)
# print(dir(djia_ext))


Point2D = namedtuple('Point2D', 'x y')

pt = Point2D(10, 20)

print(pt)
print(pt[0])
print(pt[1])
print(id(pt))
print(id(Point2D(100,pt[0])))


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
