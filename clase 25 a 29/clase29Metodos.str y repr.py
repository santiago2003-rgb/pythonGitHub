class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f'{self.name}, {self.age} años'
    
    def __repr__(self):
        return f'Person(name = {self.name}, age = {self.age})'
    
person1 = Person('Heidy', 18)
person2 = Person('Santiago', 21)

#USO DEL __STR__
print(person1)
print(person2)

#USO DEL __REPR__
print(repr(person1))
print(repr(person2))
