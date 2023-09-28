from Pets.Pet import Pet


class Dog(Pet):
    guard = False
    def __init__(self, id, name, birthdate, thoroughbred):
        super().__init__(id, name, birthdate, thoroughbred)
    def Comands(self):
        print("Выполняемые команды животного")