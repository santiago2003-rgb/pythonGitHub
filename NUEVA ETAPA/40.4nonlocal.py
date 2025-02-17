def outer_function():
    x = 'Enclosing'
    def inner_function():
        nonlocal x
        x = 'Modified'
        print(f'El valor en inner es: {x}')
    inner_function()
    print(f'El valor outer: {x}')
outer_function()
