import queue

def Item():

    def __init__(self, name, price):
        self.name = "name"
        self.price = price
        self.category = ""
    
    def update_cost(self, new_price):
        self.price = new_price

    # TODO: Store historical data better