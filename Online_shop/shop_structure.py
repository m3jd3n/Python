class Basket:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def remove(self, product):
        self.items.remove(product)
        
    def total(self):
        return sum(product.price for product in self.items)

    def __str__(self):
        return f"Basket with {len(self.items)} items"
    
class Product:
    def __init__(self, name, price, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} price: {self.price} quantity: {self.quantity}"

class Order:

    def __init__(self, basket, order_id = 0, status = "new"):
        self.basket = basket
        self.status = status
        self.order_id = order_id
        __order_status_states = ["new", "paid", "shipped", "delivered", "cancelled"]

    def __str__(self):
        return f"Order number {self.order_id} with {len(self.basket.items)} items for total of {self.basket.total()}"

    def pay(self):
        self.status = "paid"

    def ship(self):
        self.status = "shipped"

    def deliver(self):
        self.status = "delivered"

    def cancel(self):
        self.status = "cancelled"

class OrderDatabase:
    def __init__(self):
        self.orders = []
        self.order= order
        self.order_id = 0

    def add_order(self, order):
        self.order_id += 1
        order.order_id = self.order_id
        self.orders.append(order)

    def get_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def __str__(self):
        return f"Order database with {len(self.orders)} orders"

