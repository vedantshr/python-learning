class Product:
    def __init__(self, pID, pCostPrice, pSellingPrice, pProfitMargin):
        self.pID = pID.lower()
        self.pCostPrice = pCostPrice
        self.pSellingPrice = pSellingPrice
        self.pProfitMargin = pProfitMargin

    def setProfit(self):
        self.pProfitMargin = ((self.pSellingPrice-self.pCostPrice)/self.pCostPrice)*100

class Store:
    def __init__(self, storeName, productList, activeProducts):
        self.storeName = storeName
        self.productList = productList
        self.activeProducts = activeProducts

    def setProduct(self, activeIDs):
        for productID in activeIDs:
            for productObj in self.productList:
                if productID == productObj.pID:
                    productObj.setProfit()
                    self.activeProducts.append(productObj)
                    break
        return self.activeProducts

    def topProduct(self):
        maximumProfit = 0
        maxObj = None
        for actProduct in self.activeProducts:
            if maximumProfit < actProduct.pProfitMargin:
                maximumProfit = actProduct.pProfitMargin
                maxObj = actProduct
        return maxObj

if __name__ == "__main__":
    noOfProducts = int(input())
    listOfProducts = []
    for i in range(noOfProducts):
        pID = input()
        pCostPrice = float(input())
        pSellingPrice = float(input())
        productObject = Product(pID, pCostPrice, pSellingPrice, 0.0)
        listOfProducts.append(productObject)
    
    storeObj = Store("Walmart", listOfProducts, [])
    activeIDs = list(input().lower().split(" "))
    actPro = storeObj.setProduct(activeIDs)
    if actPro == []:
        print ("No product found with respectivr IDs.")
    else:
        for AP in actPro:
            print (AP.pID, "\t", AP.pProfitMargin)
    topPro = storeObj.topProduct()
    if topPro is None:
        print ("No products in Store.")
    else:
        print(topPro.pID, "\t", topPro.pProfitMargin)