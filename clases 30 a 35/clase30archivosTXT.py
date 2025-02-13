#LEER UN ARCHIVO LINEA POR LINEA
#R ES 
'''with open('archivoTXT.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())
        
#LEER TODAS LAS LINEAS EN UNA LISTA
with open('archivoTXT.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

#A ES APPEND EN TXT
#AÑADIR TEXTO 
with open('archivoTXT.txt', 'a') as file:
    file.write('\n\nBy:ChatGpt')

#SOBREESCRIBIR EL TEXTO
with open('archivoTXT.txt', 'w') as file:
    file.write('\n\nBy:ChatGpt')'''
    
#EJERCICIO
with open('archivoTXT.txt', 'r') as file:
    lineas = file.readlines()
    print(len(lineas))

