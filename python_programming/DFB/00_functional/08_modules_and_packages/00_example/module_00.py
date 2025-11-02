print('------------------- Running {0} ----------------------'.format(__name__))


def pprint(header, d):
    print('\n\n----------------------------------------')
    print('**************** {0} ******************'.format(header))
    for k, v in d.items():
        print(k,v)


pprint('module00.globals', globals())


print('--------------------- End of {0} -----------------------'.format(__name__))