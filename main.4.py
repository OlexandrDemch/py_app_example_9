try:

    end = int(input('x->'))
    symbol = '*'
    print((symbol + "") * end)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
