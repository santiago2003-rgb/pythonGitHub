import json
'''import os
print(os.getcwd())'''

with open('archivo.json', mode='r') as file:
    archives = json.load(file)
    
#MOSTRAR EL CONTENIDO 
for archive in archives:
    print(f'Archive: {archive['name']}, price {archive['price']}')