class Product:
    def __init__(self, pID, pCostPrice, pSellingPrice, pProfitMargin):
        self.pID = pID
        self.pCostPrice = pCostPrice
        self.pSellingPrice = pSellingPrice
        self.pProfitMargin = pProfitMargin
    # def setProfit(self):
    #     pProfitMargin = float(((pSellingPrice-pCostPrice)/pCostPrice)*100)
    #     profitmargin = round(pProfitMargin,2)
class Store:
    def __init__(self, storeName, productlist, activeproducts):
        self.storeName = storeName
        self.productlist = productlist
        self.activeproducts = activeproducts

if __name__ == "__main__":
    n = int(input())
    productlist = []
    activeproducts = []
    for i in range(n):
        pID = str(input()).lower()
        pCostPrice = float(input())
        pSellingPrice = float(input()) 
        pProfitMargin = float(((pSellingPrice-pCostPrice)/pCostPrice)*100)
        pProfitMargin = round(pProfitMargin,2)
        obj = Product(pID, pCostPrice, pSellingPrice, pProfitMargin)
        productlist.append(obj)
        activeproducts.append(obj.pProfitMargin)
    activeIDs = list(map(str, input().split(" ")))
    print(activeproducts)




