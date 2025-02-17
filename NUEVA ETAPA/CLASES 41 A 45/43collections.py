#count_products = defaultdict
'''from collections import defaultdict #Establece un valor por defecto

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)'''

#count_sales = Counter
'''from collections import Counter

def count_sales(products: list[str]) -> Counter:
    #Usa Counter para contar cuantos productos de cada tipo se han enviado 
    return Counter(products)

sales = ['laptop','smartphone', 'smartphone', 'laptop', 'tablet']
result = count_sales(sales)
print(result)'''

#manage_delivery = deque
from collections import deque

def manage_delivery_queue() -> deque:
    #Crear una cola para gestionar entregas de productos
    delivery_queue = deque(['order_1', 'order_2', 'order_3'])
    delivery_queue.append('order_4') #Agregar al final de la cola
    delivery_queue.appendleft('order_0') #Agrega al principio de la cola
    delivery_queue.pop() #Elimina el final 
    delivery_queue.popleft()
    return delivery_queue

queeu = manage_delivery_queue()
print(queeu)