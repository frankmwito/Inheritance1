class Electronic:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.__price = price
        self.quantity = quantity
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __str__(self):
        return f"Electronic, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, quantity:{self.quantity}"

class Laptop(Electronic):
    def __init__(self, name, brand, price, quantity, processor):
        super().__init__(name, brand, price, quantity)
        self.processor = processor

class Phone(Electronic):
    def __init__(self, name, brand, price, quantity, display_size):
        super().__init__(name, brand, price, quantity)
        self.display_size = display_size

    def __str__(self):
        return f"Phone, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, display_size:{self.display_size}"
    
    
# Instantiate a Phone object
phone1 = Phone("Smartphone", "Samsung", 1000, 2, 6.2)

# Instantiate a Laptop object
laptop1 = Laptop("Notebook", "HP", 800, 3, "Intel i5")

# Print the objects, invoking their respective __repr__ methods
print(phone1)
print(laptop1)