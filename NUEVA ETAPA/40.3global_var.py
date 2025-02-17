x = 5 #Variable global

def modify_global():
    global x
    x+=3
    print(f'Valor modficado {x}')

modify_global()
print(x)