from typing import List

class Animal:
    def __init__(self, id: int, name: str, birthdate: str):
        self.id = id
        self.name = name
        self.birthdate = birthdate

class Cat(Animal):
    def __init__(self, id: int, name: str, birthdate: str, isStray: bool):
        super().__init__(id, name, birthdate)
        self.isStray = isStray

class Donkey(Animal):
    def __init__(self, id: int, name: str, birthdate: str, age: int):
        super().__init__(id, name, birthdate)
        self.age = age

class Camel(Animal):
    def __init__(self, id: int, name: str, birthdate: str, humpCount: int):
        super().__init__(id, name, birthdate)
        self.humpCount = humpCount

class Dog(Animal):
    def __init__(self, id: int, name: str, birthdate: str, isTrained: bool):
        super().__init__(id, name, birthdate)
        self.isTrained = isTrained

class Farm:
    def __init__(self):
        self.animals = []

    def adopt(self, animal: Animal):
        self.animals.append(animal)

    def printAnimals(self):
        for animal in self.animals:
            print(f"ID: {animal.id}, Name: {animal.name}, Birthdate: {animal.birthdate}")

class Menu:
    @staticmethod
    def showMainMenu():
        print("1. Print all animals")
        print("2. Print animals of a specific class")
        print("3. Show commands")
        print("4. Add new command")
        print("5. Add new animal")

    @staticmethod
    def printOnlyThisClass(animalFarm: Farm):
        className = input("Enter the class name: ")
        for animal in animalFarm.animals:
            if type(animal).__name__ == className:
                print(f"ID: {animal.id}, Name: {animal.name}, Birthdate: {animal.birthdate}")

    @staticmethod
    def Comands():
        print("Showing commands...")

    @staticmethod
    def newComand():
        print("Adding new command...")

    @staticmethod
    def newAnimal():
        print("Adding new animal...")

if __name__ == "__main__":
    animalFarm = Farm()
    animalFarm.adopt(Cat(1009, "Мася", "2009-12-12", True))
    animalFarm.adopt(Donkey(1019, "Джек", "2019-01-12", 12))
    animalFarm.adopt(Camel(1091, "Горбун", "2016-07-15", 15))
    animalFarm.adopt(Dog(1209, "Байкал", "2018-07-15", False))
    while True:
        Menu.showMainMenu()
        i = int(input())
        if i == 1:
            animalFarm.printAnimals()
        elif i == 2:
            Menu.printOnlyThisClass(animalFarm)
        elif i == 3:
            Menu.Comands()
        elif i == 4:
            Menu.newComand()
        elif i == 5:
            Menu.newAnimal()