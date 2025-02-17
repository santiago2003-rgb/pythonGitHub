from typing import List, Dict

def empleado_por_sueldo(empleados: List[Dict[str, int]], sueldo_minimo: float) -> List[Dict[str, int]]:
    return [empleado for empleado in empleados if float(empleado['sueldo']) > sueldo_minimo]

empleados = [
    {
        'mombre': 'Santiago Mejia',
        'edad': 21,
        'sueldo': 30000 
    },
    {
        'mombre': 'Heidy Quiceno',
        'edad': 18,
        'sueldo': 25000 
    },
    {
        'mombre': 'Ares Mejia Quiceno',
        'edad': 20,
        'sueldo': 20000 
    },
    {
        'mombre': 'Sebastian',
        'edad': 30,
        'sueldo': 50000 
    }
]

print(empleado_por_sueldo(empleados, 25000))