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


from decimal import Decimal

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

# Write general decorator: Single dispatch

def singledispatch(fn):
    registry = {}

    registry[object] = fn

    def inner(args):
        return registry[object](args)

    return inner

@singledispatch
def htmlize(a):
    return escape(str(a))

# print(htmlize('1 < 100'))


# Expand the decorator


def singledispatch(fn):
    registry = {}

    registry[object] = fn
    registry[int] = lambda a: '{0}(<i>({1})</i>)'.format(a, str(hex(a)))
    registry[str] = lambda s: escape(s).replace('\n', '<br/>\n')

    def inner(args):
        return registry.get(type(args), registry[object])(args)

    return inner


@singledispatch
def htmlize(a):
    return escape(str(a))

# print(htmlize('1 < 100'))
# print(htmlize(100))


#  removing hard-coded registry
def singledispatch(fn):
    registry = {}

    registry[object] = fn

    def decorated(args):
        return registry.get(type(args), registry[object])(args)

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorated.register = register
    # decorated.registry = registry
    decorated.dispatch = dispatch
    return decorated


@singledispatch
def htmlize(a):
    return escape(str(a))
#
# print(htmlize('1 < 100'))
# print(htmlize(100))
#

@htmlize.register(int)
def html_int(a):
    return '{0}(<i>({1})</i>)'.format(a, str(hex(a)))

# print(htmlize('1 < 100'))
print(htmlize(100))
print(htmlize.dispatch(100))

# for a list
@htmlize.register(list)
def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
# print(htmlize(100))

html_list =htmlize.register(list)(html_list)

# We can stak
@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
# print(htmlize(100))

print(htmlize([1,2,3]))
print(htmlize((1,2,3)))
# print(htmlize.registry)
print(htmlize(True))


from collections.abc import Sequence

print(isinstance([1,2,3], Sequence))

@htmlize.register(Sequence)

def html_sequence(l):
    items = ('<li>{0}</li>'.format(html_escape(item))
             for item in l
             )

    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print(type([1,2,3]) is Sequence)
# OPTIMIZE
# TODO
# FIXME
