import random

#GENERAR UN NUMERO ENTERO ALEATORIO
'''randomNumber = random.randint(1, 10) #randint es un numero entero aleatorio
print(randomNumber)'''

#ELEGIR COLORES ALEATORIOS
'''colors = ['Rojo', 'Azul', 'Verde']
randomColor = random.choice(colors)
print(randomColor)'''

#BARAJAR UNA LISTA DE CARTAS
cards = ['As', 'Rey', 'Reina', 'Jota', '10']
random.shuffle(cards)
print(cards)