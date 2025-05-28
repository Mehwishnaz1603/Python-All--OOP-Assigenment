#--------Assigenment 18---------#
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, 
# and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value


    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price


product = Product(100)

print("Price:", product.price)

product.price = 150
print("Updated Price:", product.price)

product.price = -50

del product.price
