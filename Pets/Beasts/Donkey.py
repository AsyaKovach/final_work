from Pets.Beasts.Beast import Beast


class Donkey(Beast):
    def __init__(self, id, name, birthdate, loadCapacity):
        super().__init__(id, name, birthdate, loadCapacity)
    
    def Comands(self):
        print("Выполняемые команды животного")