class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self, storename, address, products):
        self.storename = storename
        self.address = address
        self.products = products

if __name__ == "__main__":
    n = int(input())
    l = []
    products = []
    for i in range(n):
        name = str(input())
        price = float(input())
        quantity = int(input())
        obj = Product(name, price, quantity)
        products.append(obj)
        l.append(obj.TotalPrice())
    print("\n",l)
        
        



