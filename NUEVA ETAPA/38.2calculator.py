class Calculator:
    def add_numbers(self, first_numbers, second_numbers):
        result = first_numbers + second_numbers
        return result
    
calc = Calculator()
print(calc.add_numbers(5, 3))