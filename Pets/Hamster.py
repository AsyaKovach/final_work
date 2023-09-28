from Pets.Pet import Pet


class Hamster(Pet):
    def __init__(self, id, name, birthdate, thoroughbred):
        super().__init__(id, name, birthdate, thoroughbred)
    def Comands(self):
        print("Это животное не выполняет команд")