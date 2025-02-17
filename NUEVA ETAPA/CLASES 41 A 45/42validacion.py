#VALIDACIONES
def divide(a: int, b: int) -> float:
    #Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parametros deben ser enteros')
    #Verificamos que el divisor no sea cero
    if b == 0:
        raise ValueError('El divisor no puede ser cero')
    return a / b
    
#Ejemplo de uso 
try:
    res = divide(10, '2') #Error de tipo
    print(res)
except TypeError as e:
    print(f'Error: {e}')
try:
    res1 = divide(10, 0) #Error de divisor cero
    print(res1)
except ValueError as a:
    print(f'Error: {a}')
try:
    res3 = divide(10, 2) #Divison correcta
    print(res3)
except (ValueError, TypeError) as s:
    print(f'Error: {e}')