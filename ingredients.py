class Ingredient:

    def __init__(self):
        self.name()
        self.quantity()
        self.unit()
        
    def name(self):
        while True:
            try:
                self.name = input("\n      Ingredient name: ").capitalize()
                return self.name
            except ValueError:
                print("          -- Invalid name, please try again. --")

    def quantity(self):
        while True:
            try:
                self.quantity = float(input("      Quantity: "))
                return self.quantity
            except ValueError:
                print("          -- Invalid quantity, please use numbers only. --")

    def unit(self):
        while True:
            self.unit = input("      Unit: ").lower()
            if self.unit.isalpha():
                return self.unit
            else:
                print("          -- Invalid unit, please try again. --")
