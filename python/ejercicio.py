'''def lista_empleados(lista, limite_salarios):
    resultados = []
    for k in range(len(lista)):
        if lista[k]['Salario'] > limite_salarios:
            resultados.append(lista[k]['Name'])
    return resultados'''
    
#Otra solucion del reto
employes = [
    
    {
        'name':'Jose',
        'age': 30,
        'salary': 2800
    },
    {
        'name':'Marcos',
        'age': 25,
        'salary': 3500
    },
    {
        'name':'Santiago',
        'age': 21,
        'salary': 4200
    },
    {
        'name':'Heidy',
        'age': 18,
        'salary': 5600
    },
    {
        'name':'Sebas',
        'age': 42,
        'salary': 1500
    }
]

def paid_employes(employes):
    best_paid = []
    for i in employes:
        if i['salary'] > 3000:
            best_paid.append(i['name']) # Guarda los mejores pagos
            best_paid.sort()
    print(f'Los empleados que mas ganan son: {best_paid}')
    
paid_employes(employes)