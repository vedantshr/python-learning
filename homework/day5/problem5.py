class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Store:
    def __init__(self, nameS, address, products):
        self.nameS = nameS
        self.address = address
        self.products = products
    
    def totalProductionPriceForCategory(self, category):
        for objects in self.products:
            if category == objects.name:
                return objects.price*objects.quantity

    def checkProductAvailability(self, nameOfpro):
        dict1 = {}
        for objects in self.products:
            if nameOfpro == objects.name:
                if objects.quantity > 0:
                    status = "Available"
                    dict1[objects.name] = status
                    return dict1
                elif object.quantity == 0:
                    status = "Out of stock"
                    dict1[objects.name] = status
                    return dict1
            else:
                status = "Not Available"
                dict1[nameOfpro] = status   

if __name__ == "__main__":
    noOfProducts = int(input())
    products = []
    for i in range(noOfProducts):
        name = input()
        price = float(input())
        quantity = int(input())
        obj = Product(name, price, quantity)
        products.append(obj)
    
    
    objStore = Store("General Store", "Paschim Vihar", products)
    category = input()
    nameOfpro = input()    
    catg = objStore.totalProductionPriceForCategory(category)
    availability = objStore.checkProductAvailability(nameOfpro)
    print(catg) 
    print(availability)

    



