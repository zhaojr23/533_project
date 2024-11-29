class sales():
    """
    A class to manage sales-related operations, including products on shelves.

    Attributes:
    ----------
    shelves : dict
        A dictionary containing products currently on shelves, including their details.
    product : Warehouse
        An instance of the Warehouse class to interact with the warehouse inventory.

    Methods:
    -------
    add_newproduct(self, productId, quantity, saleprice):
        Adds a new product from the warehouse to the shelves and updates the stock.
    increase_quantity(self, productId, quantity):
        Increases the quantity of a product on shelves and reduces it from the warehouse.
    decrease_quantity(self, productId, quantity):
        Decreases the quantity of a product on shelves and returns it to the warehouse.
    change_price(self, productId, newprice):
        Updates the sale price of a product on shelves.
    display(self):
        Displays details of all products currently on shelves.
    """
    def __init__(self,product):
        self.shelves={}
        self.product = product
    def add_newproduct(self, productId, quantity, saleprice):
        if productId not in self.shelves and productId in self.product.products and quantity <= self.product.products[productId]["quantity"]:
            self.shelves[productId]={
                "name": self.product.products[productId]["name"],
                "quantity": quantity,
                "sprice" : saleprice,
                "pprice" : self.product.products[productId]["pprice"]
            }
            self.product.remove_product(productId, quantity)
        else:
            print("On shelves or wrong productId or quantity is too large")

    def increase_quantity(self, productId, quantity):
        if productId in self.shelves and quantity <= self.product.products[productId]["quantity"]:
            self.shelves[productId]["quantity"] += quantity
            self.product.remove_products(productId, quantity)
        else:
            print("This product is not on the shelves")

    def decrease_quantity(self, productId, quantity):
        if productId in self.shelves and quantity <= self.shelves[productId]["quantity"]:
            self.shelves[productId]["quantity"] += quantity
            self.product.products[productId]["quantity"] += quantity
        else:
            print("This product is not on the shelves")
    def change_price(self, productId, newprice):
        if productId in self.shelves:
            self.shelves[productId]["sprice"] = newprice
        else:
            print("This product is not on the shelves")
    def display(self):
         for id, product in self.shelves.items():
            print(id, product['name'], product['quantity'], product['sprice'])
    