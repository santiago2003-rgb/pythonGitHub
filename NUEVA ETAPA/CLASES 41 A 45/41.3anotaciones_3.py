#ANOTACION 3 
class Employee:
    name: str
    age: int
    salary: float
    
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
        
    
    def introducce(self) -> str:
        return f'Hola, me llamo {self.name} y tengo {self.age} años'
    
employee1 = Employee('Santiago', 30, 3500.00)
print(employee1.introducce())