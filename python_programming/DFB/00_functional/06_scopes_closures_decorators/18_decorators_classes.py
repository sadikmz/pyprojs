# Overloadding of function: names function with the same name but distinct signatures (based on the types and number of parameters)
# Single dispatch generic functions
# Multiple dispatch generic functions

from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br>\n')

def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(k,v)
             for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# addition: non-being passed etc


print(html_str("""This is a multiline
string with special 
charactor 10 < 100
"""))


print(html_int(255))
print(html_escape(3+10j))


from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)


print(htmlize(3.14))
print(htmlize("""Python 
rocks!
"""))

print(htmlize([1,3,4]))
print(htmlize(["""Python 
rocks!""", 0<1, (10,20,30),100]))



#
def htmlize(arg):
    registry = {
        object : html_escape,
        int : html_int,
        float : html_real,
        Decimal : html_int,
        str : html_str,
        list : html_list,
        tuple: html_list,
        dict : html_dict,
        # set : html_set
    }

    fn = registry.get(type(arg), registry[object])
    return fn(arg)

print(htmlize(100))
print(htmlize([1,2,3]))