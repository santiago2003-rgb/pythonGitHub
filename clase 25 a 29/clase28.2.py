class livingBeing:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, age): #CONSTRUCTOR
        super().__init__(name)
        self.age = age #ATRIBUTOS
        
class Student(Person):
    def __init__(self, name, age, studentId):
        super().__init__(name, age)
        self.studentId = studentId
    
    def introduce(self):
        print(f'Hi, im {self.name}, {self.age} years old, and my student ID is {self.studentId}')
        
student = Student('Santiago', 20, 's123')
student.introduce()