from Pets.Beasts.Beast import Beast


class Horse(Beast):
    def __init__(self, id, name, birthdate, loadCapacity):
        super().__init__(id, name, birthdate, loadCapacity)
        self.saddle = None

    def Comands(self):
        print("Выполняемые команды животного")