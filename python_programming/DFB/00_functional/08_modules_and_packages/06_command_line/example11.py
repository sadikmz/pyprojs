# sentinel values of parameter defaults

def validate(a = object(), b = object(), *, kw = object ()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_kw = validate.__kwdefaults__['kw']

    print(default_a is default_b)
    print(default_b is default_kw)

    if a is not default_a:
        print('Argument a was provided')
    else:
        print('Argument a was not provided')

    if b is not default_b:
        print('Argument b was provided')
    else:
        print('Argument b was not provided')

    if kw is not default_kw:
        print('Argument kw was provided')
    else:
        print('Argument kw was not provided')


validate(100,200,kw=300)
# validate(100,200,kw=300)