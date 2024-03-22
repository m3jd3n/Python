
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_products(self):
        print("Listing products:")
        for product in self.products:
            print(product)

    def get_product(self, product_name):
        for product in self.products:
            if product.name.upper() == product_name.upper():
                return product
        return None

    def __str__(self):
        return f"Shop with {len(self.products)} products"


class Basket:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def remove(self, product):
        self.items.remove(product)

    def is_empty(self):
        return len(self.items) == 0
        
    def total(self):
        return sum(product.price for product in self.items)

    def __str__(self):
        return f"Basket with {len(self.items)} items"

    def basket_items_list(self):
        print("Basket items:")
        for item in self.items:
            print(item)

    
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return f"{self.name} price: {self.price}"


class Order:

    def __init__(self, basket, order_id = 0, status = "new"):
        self.basket = basket
        self.status = status
        self.order_id = order_id
        __order_status_states = ["new", "paid", "shipped", "delivered", "cancelled"]

    def __str__(self):
        return f"Order number {self.order_id} with {len(self.basket.items)} items for total of {self.basket.total()} and status: {self.status}"

    def get_status(self):
        return self.status

    def order_items_list(self):
        print("Order items:")
        self.basket.basket_items_list()


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

    def list_orders(self):
        if not self.orders:
            print("No orders found")
            return
        else:
            print("Listing orders:")
            for order in self.orders:
                print(order)

    def __str__(self):
        return f"Order database with {len(self.orders)} orders"

