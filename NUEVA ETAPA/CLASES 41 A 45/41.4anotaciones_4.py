from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    '''
    Busca un ID empleado en una lista de IDS y devuelve el valor si existe
    
    Parametros:
    employee_ids(list[int]): Lista de IDS de empleado
    employee_id(int): ID a buscar 
    
    Retorna:
    Optional[int]: El ID encontrado o none si no existe en la lista 
    '''
    if employee_id in employee_ids:
        return employee_id
    return None