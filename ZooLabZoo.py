#Zoo Lab Project: Zoo

class Zoo:

    def __init__(self, n, p, io, e):
        self.name = n
        self.price = p
        self.isopen = io
        self.enclosures = e

    def __str__(self):
        return f"Name: {self.name} | Price: {self.price} | Status: {self.isopen} | Enclosures: {self.enclosures}"
    
    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getIsOpen(self):
       return "Open" if self.isopen else "Closed"

    def getEnclosures(self):
        return self.enclosures
