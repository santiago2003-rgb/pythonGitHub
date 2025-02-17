x = 100 #Variable global

def local_function():
    x = 10 #Variables de tipo local
    print(f'El valor de la variable es: {x}')
    
    
def show_globlal():
    print(f'El valor de la variablo gobla es {x}')

#local_function()
print(x) #Genera error

