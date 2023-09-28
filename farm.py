from typing import TypeVar, List
from Pets.Beasts.Beast import Beast

from Pets.Pet import Pet

class Farm:
    def __init__(self):
        self.animals = []

    def adopt(self, animal):
        self.animals.append(animal)
        return True

    def release(self, animalFarm):
        if animalFarm in self.animals:
            self.animals.remove(animalFarm)
            return animalFarm
        return None

    @staticmethod
    def create():
        return Farm()

    @staticmethod
    def adopt(farm, animal):
        return farm.adopt(animal)

    def printOnlyThisClass(self, animalClass):
        if animalClass == 1:
            self.printCollection(Pet)
        elif animalClass == 2:
            self.printCollection(Beast)

    def printCollection(self, choiseClass):
        for animal in self.animals:
            if isinstance(animal, choiseClass):
                print(animal)

    def printAnimals(self):
        for animal in self.animals:
            print(animal)