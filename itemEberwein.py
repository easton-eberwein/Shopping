"""
File: itemEberwein.py
This module defines the Rectangle class
"""

class Item:
    """This class represents an item's name, quantity and unit price"""

    def __init__(self, name, quantity, price):
        self.myName = name
        self.myQuantity = quantity
        self.myPrice = price

    def __str__(self):
        """Returns the string representation for an item"""
        result = "" + str(self.myName) + "\n"
        result += "The quantity is: " + str(self.myQuantity) + "\n"
        result += "The price is: $" + str(self.myPrice) + "\n"
        return result

    def getName(self):
        """Returns the name of the item"""
        return self.myName

    def getQuantity(self):
        """Returns the quantity of the item"""
        return self.myQuantity

    def getPrice(self):
        """Returns the unit price of the item"""
        return self.myPrice

    def setName(self, name):
        """Sets the name of the item"""
        return self.myName

    def setQuantity(self, quantity):
        """Sets the quantity of the item"""
        return self.myQuantity

    def setPrice(self, price):
        """Sets the unit price of the item"""
        return self.myPrice

    
