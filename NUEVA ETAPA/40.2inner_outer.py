x = 'Global' #Variable global

#Funcion externa
def outer_function():
    x = 'Enclosing'
    
    #Funcion interna
    def inner_function():
        x = 'Local' #Variable local
        print(x)
        
    inner_function()
    print(x)

outer_function()
print(x)

