# QUESTION 4: PRODUCT PRICE VALIDATION
#
# Create a class called Product.
#
# Requirements:
# 1. The class should contain:
#    - name
#    - private variable __price
#
# 2. Use __init__() to initialize the product name
#    and price.
#
# 3. Create a getter using @property
#    to access the price.
#
# 4. Create a setter using @price.setter
#    to update the price.
#
# 5. The setter should allow the price only when:
#       price > 0
#
# 6. If the user gives 0 or a negative price,
#    print:
#       "Invalid price"
#
# 7. Create a Product object.
#
# 8. Print its price using:
#       product.price
#
# 9. Change the price using:
#       product.price = new_price
#
# 10. Try assigning an invalid price.
#
# Concepts to practice:
# - Encapsulation
# - Private variables
# - @property
# - Getter
# - Setter
# - Data validation
class Product:
    def __init__(self,name,price):
        self.name=name
        self.__price=price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if self.__price<=new_price:
            self.__price=new_price
            print(f"Rs.{new_price} Price is updated")
        else:
            print("Invalid Price")

p1=Product("Laptop",60000)
p1.price=-788
print(p1.price)
print('\n')
p1.price=890000
print(p1.price)