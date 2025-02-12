class Person:
    def __init__(self, name, age): #CONSTRUCTOR
        self.name = name #ATRIBUTOS
        self.age = age #ATRIBUTOS
        
    def greet(self):
        print('Hello im person')
        
class Student(Person):
    def __init__(self, name, age, studentId):
        super().__init__(name, age)
        self.studentId = studentId
    
    def greet(self):
        super().greet()
        print(f'Hello, my student ID is {self.studentId}')
        
student = Student('Santiago', 20, 's123')
student.greet()