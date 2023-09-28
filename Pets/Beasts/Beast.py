from Pets.Beasts.Employable import Employable
from animal import Animal

class Beast(Animal, Employable):
    
    def __init__(self, id, name, birthdate, loadCapacity):
        super().__init__(id, name, birthdate)
        self.loadCapacity = loadCapacity
    
    def getLoadCapacity(self):
        return self.loadCapacity
    
    def setLoadCapacity(self, loadCapacity):
        self.loadCapacity = loadCapacity
    
    def employ(self):
        pass
    
    def __str__(self):
        return "id: {}\nName: {}\nРожден: {}\nГрузоподъемность: {}\n".format(self.getId(), self.getName(), self.getBirthdate(), self.loadCapacity)
