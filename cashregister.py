class CashRegister:
    # constructor, initialize instance variables
    def __init__(self, taxRate):
        self._totalPrice = 0.0
        self._itemCount = 0
        self._taxableTotal = 0.0
        self._taxRate = taxRate

    # @param price, price of this item
    # @param taxable, True if item is taxable
    def add_item(self, price, taxable):
        self._itemCount += 1
        self._totalPrice += price
        if taxable:
            self._taxableTotal += price

    def get_total(self):
        return self._totalPrice + self._taxableTotal * self._taxRate / 100

    def get_count(self):
        return self._itemCount

    # clears cash register
    def clear(self):
        self._totalPrice = 0
        self._itemCount = 0
        self._taxableTotal = 0.0


# TESTER
register1 = CashRegister(2)
register1.add_item(32.6, True)
register1.add_item(12.5, False)
register1.add_item(45.87, False)
register1.add_item(19.45, True)
print("Count:", register1.get_count())
print("Total $%.2f" % register1.get_total())
