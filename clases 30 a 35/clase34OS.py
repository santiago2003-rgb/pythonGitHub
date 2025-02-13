import os

'''cwd = os.getcwd()
print('Directorio de trabajo actual', cwd)'''

#LISTAR LOS ARCHIVOS .TXT
txtFiles = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Archivos txt son: ', txtFiles)

#RENOMBRAR ARCHIVO
os.rename('archivoTXT.txt', 'cuento.txt')
print('Archivo renombrado')

#LISTAR LOS ARCHIVOS .TXT
txtFiles = [f for f in os.listdir('.') if f.endswith('.txt')]
print('Archivos txt son: ', txtFiles)