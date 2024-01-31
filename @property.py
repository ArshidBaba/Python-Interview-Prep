class House:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price


# Iniatilization
house = House(45000)  # Create instance

# Getter
# price = house.price  # Access value
# print(price)

# Setter
# house.price = 50000.0
# price = house.price
# print(price)

# Deleter
del house.price
price = house.price

print(price)
