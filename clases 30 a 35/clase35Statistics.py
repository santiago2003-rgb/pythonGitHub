import statistics
import csv

#LEER LOS DATOS DE VENTAS MENSUALES DESDE UN ARCHVIO CSV
monthlySales = {}
with open('monthly.csv', mode = 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthlySales[month] = sales
    
sales = list(monthlySales.values())
print(sales)

#HALLAR LA MEDIA = mean
meanSales = statistics.mean(sales)
print(f'La media es: {meanSales}')

#HALLAR LA MEDIANA = median
medianSales = statistics.median(sales)
print(f'La mediana es: {medianSales}')

#HALLAR LA MODA = mode
modeSales = statistics.mode(sales)
print(f'La moda es: {modeSales}')

#HALLAR LA DESVIACION ESTANDAR = stedv
stdevSales = statistics.stdev(sales)
print(f'La desviacion estandar es: {stdevSales}')

#HALLAR LA VARIANZA = variance
varianceSales = statistics.variance(sales)
print(f'La varianza es: {varianceSales}')

#MAXIMO, MINIMOS Y RANGO = max(), min() y range = max - min
maxSales = max(sales)
minSales = min(sales)

rangeSales = maxSales - minSales
print(f'Rango de ventas: {rangeSales}')