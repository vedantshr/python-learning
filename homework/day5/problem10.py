class FoodItem:
    def __init__(self, item_id, item_name, item_category, item_price):
        self.item_id = item_id
        self.item_name = item_name
        self.item_category = item_category
        self.item_price = item_price

    def provideDiscount(self, discountPercentage):
        for objects in fooditem_list:
            if nameOfItem == objects.item_name:
                return (objects.item_price - (objects.item_price*discountPercentage)/100)
    
class Restaurant:
    def __init__(self, restaurant_name, fooditem_list):
        self.restaurant_name = restaurant_name
        self.fooditem_list = fooditem_list  

    def retrieveUpdatedPrice(self, updatePercentage):
        for objects in self.fooditem_list:
            if itemId == objects.item_id:
                return (objects.item_price - (objects.item_price*updatePercentage)/100)

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
    
    discountPercentage = float(input())
    nameOfItem = input()
    itemId = int(input())
    updatePercentage = float(input())
    obj2 = Restaurant("Moti Mahal", fooditem_list)
    discPercentage = obj.provideDiscount(discountPercentage)
    updatedPrice = obj2.retrieveUpdatedPrice(updatePercentage)
    print(discPercentage)
    print(updatedPrice)

