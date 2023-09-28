from Pets.Pet import Pet


class Cat(Pet):
    def __init__(self, id, name, birthdate, thoroughbred):
        super().__init__(id, name, birthdate, thoroughbred)
    
    def commands(self):
        print("Выполняемые команды животного")