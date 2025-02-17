from typing import Union #Union nos permite de que sea de dos tipos de datos entero o flotante y no None

def process_salary(salary: Union[int, float]) -> float:
    '''
    Procesa un salario que puede ser entero o flotante y lo devuleve como flotante
    
    Parametros:
    Salary(Union[int, float]): Un salario que puede ser un entero o flotante
    
    Retorna:
    float: El salario convertido a flotante
    '''
    return float(salary)