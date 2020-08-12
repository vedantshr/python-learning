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
        totalPrice = 0
        for objects in self.products:
            if category == objects.name.split("-")[0]:
                totalPrice = totalPrice + (objects.price*objects.quantity)
        return totalPrice

    def checkProductAvailability(self, nameOfpros):
        dict1 = {}
        for product in nameOfpros:
            for objects in self.products:
                if product == objects.name:
                    if objects.quantity > 0:
                        status = "Available"
                        dict1[objects.name] = status
                        
                    elif object.quantity == 0:
                        status = "Out of stock"
                        dict1[objects.name] = status
        return dict1

    def calculateBill(self, listOfProducts):
        dict1 = self.checkProductAvailability(listOfProducts)
        totalBill = 0
        for products in dict1:
            for objects in self.products:
                if products == objects.name and dict1[products] == "Available":
                    totalBill += objects.price
        return totalBill
                    

                

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
    nameOfpros = input().split(" ")
    catg = objStore.totalProductionPriceForCategory(category)
    
    bill = objStore.calculateBill(nameOfpros)
    print(catg) 
    print(bill)

    



