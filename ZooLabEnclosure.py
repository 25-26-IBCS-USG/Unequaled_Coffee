class Enclosure:

    def __init__(self, b, i, a):
        
        self.biome = b
        self.info = i
        self.animals = a

    def getBiome(self):
        return self.biome

    def getInfo(self):
        return self.info

    def getAnimals(self):
        return self.animals
