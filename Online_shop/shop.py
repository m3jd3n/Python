import shop_structure

def add_to_basket(shop, basket):
    input_product = input("Enter product name to add to basket: ");
    product_obj = shop.get_product(input_product)
    print(product_obj)

    if product_obj:
        print(f"Adding product: {product_obj.name} to basket...")
        basket.add(product_obj)
    else:
        print("Product not found")

def create_order(shop, basket, order_database):
    if not basket.is_empty():
        print("Creating order...")
        order = shop_structure.Order(basket)
        order_database.add_order(order)
    else:
        print("Basket is empty")
        return

def main():
    shop = shop_structure.Shop()
    shop.add_product(shop_structure.Product("Apple", 10))
    shop.add_product(shop_structure.Product("Banana", 5))
    shop.add_product(shop_structure.Product("Orange", 8))
    shop.add_product(shop_structure.Product("Pineapple", 15))

    shop.list_products()

    basket = shop_structure.Basket()

    add_to_basket(shop, basket)
    add_to_basket(shop, basket)

    print(basket)

    order_database = shop_structure.OrderDatabase()

    create_order(shop, basket, order_database)

    print(order_database)

    print("Listing orders:")
    order_database.list_orders()

    print("Listing order items fro order database:")
    order_database.orders[0].basket.basket_items_list()

if __name__ == "__main__":
    main()