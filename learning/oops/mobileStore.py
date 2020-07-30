class mobile:
    def __init__(self, brand, price, stock, mobName):
        self.brand = brand
        self.price = price
        self.stock = stock
        self.mobName = mobName

class mobilestore:
    def __init__(self, storename, listOfmobiles):
        self.storename = storename
        self.listOfmobiles = listOfmobiles
    
    def cheapestMobile(self):
        mintemp = self.listOfmobiles[0].price
        cheapestMobile = self.listOfmobiles[0]

        for index in range(1, len(self.listOfmobiles)):
            if mintemp > self.listOfmobiles[index].price:
                mintemp = self.listOfmobiles[index].price
                cheapestMobile = self.listOfmobiles[index]

        return cheapestMobile
    
    def availability(self,mobilename):
        for mobile in self.listOfmobiles:
            if mobile.mobName == mobilename:
                if mobile.stock > 0:
                    return True
                else:
                    return False
        
        return "Mobile name does not exist"

    def brandname(self,brand):
        l1 = []
        for mobile in self.listOfmobiles:
            if mobile.brand == brand:
                l1.append(mobile)
        if len(l1) > 0:
            return l1
        else:
            return "Mobile doesn't exist for the given brand name"
                

            

if __name__ == "__main__":
    n = int(input())
    l = []
    for i in range(n):
        brand = input()
        price = float(input())
        stock = int(input())
        mobName = input()
        obj = mobile(brand, price, stock, mobName)
        l.append(obj)
    
    obj2 = mobilestore("ABC store", l)
    # cheap = obj2.cheapestMobile()

    # print (cheap.mobName, "\t", cheap.brand, "\t", cheap.price)
    # ip = input()
    # print(obj2.availability(ip))

    ip1 = input()
    x = obj2.brandname(ip1)
    if type(x) is list:
        for mobile in x:
            print(mobile.mobName , end=" ")
    else:
        print(x)
    print ()
    # m = list()

    


