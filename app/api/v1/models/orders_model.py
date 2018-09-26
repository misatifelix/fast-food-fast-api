from .base import BaseModel

"""
    Database
    List with dictionairies emulates a database table
"""
class OrderModel(BaseModel):
    existing_data = []

    def __init__(self):
       self.orders = []
       self.foods =  []
    """
    Model Managers
    """
    # get all orders
    def get_orders(self):
        return self.orders
    
    #get all food items
    def get_foods(self): 
        return self.foods

    #add an order to table
    def add_order(self,data):
        self.orders.append(data)

    #add a food item to table
    def add_foods(self,data):
        self.foods.append(data)

    
    #get total price
    def calculate_total_price(self, price, quantity):
        return price * quantity


#class instance
order_obj = OrderModel()
