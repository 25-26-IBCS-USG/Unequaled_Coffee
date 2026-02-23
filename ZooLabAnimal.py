#Zoo Lab Project: Animal File

class Animal:

    def __init__(self, n, ff):
        self.name = n
        self.funfact = ff

    def __str__(self):
        return f"Name: {self.name} | Fun Fact: {self.funfact}"

    def getName(self):
        return self.name

    def getFunfact(self):
        return self.funfact

