class Product:

    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.__price = price
        self.__stock = stock

    # Getter for price
    @property
    def price(self):
        return self.__price

    # Setter for price
    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid Amount")

    # Getter for stock
    @property
    def stock(self):
        return self.__stock

    # Setter for stock
    @stock.setter
    def stock(self, update_stock):
        if update_stock >= 0:
            self.__stock = update_stock
        else:
            print("Invalid Stock")

    # Display product details
    def display(self):
        print("Product ID :", self.product_id)
        print("Name :", self.name)
        print("Category :", self.category)
        print("Price :", self.price)
        print("Stock :", self.stock)

    # Sell product
    def sell(self, quantity):
        if quantity <= 0:
            print("Invalid Quantity")
        elif quantity > self.__stock:
            print("Not Enough Stock")
        else:
            self.__stock -= quantity
            print("Product Sold Successfully")


# Create object
p1 = Product(101, "Laptop", "Electronics", 50000, 10)

# Display initial details
p1.display()

# Get price
print("Current Price :", p1.price)

# Update price
p1.price = 55000

# Update stock
p1.stock = 20

# Sell products
p1.sell(5)

# Display updated details
print("\nAfter Updates:")
p1.display()