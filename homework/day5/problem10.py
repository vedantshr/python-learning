class FoodItem:
    def __init__(self, item_id, item_name, item_category, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_category = item_category
        self.item_price = item_price

    def provideDiscount(self, discountPercentage):
        return (self.item_price - (self.item_price*discountPercentage)/100)
    
class Restaurant:
    def __init__(self, restaurant_name, fooditem_list):
        self.restaurant_name = restaurant_name
        self.fooditem_list = fooditem_list  

    def retrieveUpdatedPrice(self, updatePercentage, itemId):
        for objects in self.fooditem_list:
            if itemId == objects.item_id:
                objects.item_price = objects.provideDiscount(updatePercentage)
                return objects

if __name__ == "__main__":
    n = int(input())
    fooditem_list = []
    for i in range(n):
        item_id = int(input())
        item_name = input()
        item_category = input()
        item_price = float(input())
        obj = FoodItem(item_id, item_name, item_category, item_price)
        fooditem_list.append(obj)
    

    itemId = int(input())
    updatePercentage = float(input())
    obj2 = Restaurant("Moti Mahal", fooditem_list)
    
    updatedPrice = obj2.retrieveUpdatedPrice(updatePercentage, itemId)
    
    print(updatedPrice.item_name, updatedPrice.item_price)

