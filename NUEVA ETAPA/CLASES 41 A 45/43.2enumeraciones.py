from enum import Enum

class OrderStatus(Enum):
    PEDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado
    
def check_order_status(status: OrderStatus):
    #Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PEDING:
        return f'Order is still pending'
    elif status == OrderStatus.SHIPPED:
        return f'Order has been shipped'
    elif status