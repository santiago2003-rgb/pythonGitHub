#Polimorfismo
class Animal:
    def hacerSonido(self):
        print('El animal hace un sonido')
        
class Perro(Animal):
    def hacerSonido(self):
        print('El perro ladra')
        
class Gato(Animal):
    print('El gato maulla')
    
def emitirSonido(animal: Animal):
    animal.hacerSonido()
    
miPerro = Perro()
miGato = Gato()

emitirSonido(miPerro)
emitirSonido(miGato)



