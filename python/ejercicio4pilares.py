from abc import ABC, abstractclassmethod
#Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    #METODOS GETTER PARA ACCEDER A LA INFORMACION
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerEdad(self):
        return self.edad
    
    #METODO SETTER PARA MODIFICAR LOS ATRIBUTOS
    def establecerNombre(self, nombre):
        if len(nombre) > 0:
            nombre = nombre
        else:
            print('El nombre no puede estar vacio')
    
    def establecerEdad(self, edad):
        if edad > 0:
            edad = edad
        else:
            print('La edad debe ser mayor a 0')
    
    @abstractclassmethod
    def saludar(self):
        pass

#CLASE EMPLEADO QUE HEREDA DE PERSONA
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto
        
    #METODO GETTER Y SETTER PARA EL ATRIBUTO PUESTO
    def obtenerPuesto(self):
        return self.puesto
    
    def establecerPuesto(self, puesto):
        self.puesto = puesto
        
    def saludar(self):
        print(f'Hola soy {self.obtenerNombre()}, tengo {self.obtenerEdad()} años y trabajo como {self.puesto}')

#CLASE ESTUDIANTE QUE HEREDA DE PERSONA
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    #METODO GETTER Y SETTER PARA EL ATRIBUTO CARRERA
    def obtenerCarrera(self):
        return self.carrera
    
    def establecerCarrera(self, carrera):
        self.carrera = carrera
        
    def saludar(self):
        print(f'Hola soy {self.obtenerNombre()}, tengo {self.obtenerEdad()} años y estudio {self.carrera}')

#FUNCION PARA HACER EL SALUDO, DEMOSTRANDO POLIMORFISMO
def hacerSaludo(persona: Persona):
    persona.saludar()
    
#CREANDO INSTANCIAS
empleado1 = Empleado('Juan', 35, 'Desarrollador')
estudiante1 = Estudiante('Ana', 22, 'Medico')

#LLAMADO A LA FUNCION HACERSALUDO
hacerSaludo(empleado1)
hacerSaludo(estudiante1)

#MODIFICANDO ATRIBUTOS A TRAVES DE LOS METODOS GETTER Y SETTER
empleado1.establecerPuesto('Gerente')
print(empleado1.obtenerPuesto())

#ACCEDIENDO A ATRIBUTOS PRIVADOS A TRAVES DE GETTERS
print(estudiante1.obtenerNombre())
