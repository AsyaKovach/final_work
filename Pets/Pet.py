from Pets.Playable import Playable
from animal import Animal


class Pet(Animal, Playable):
    def __init__(self, id, name, birthdate, thoroughbred):
        super().__init__(id, name, birthdate)
        self.thoroughbred = thoroughbred
    
    def getThoroughbred(self):
        return self.thoroughbred
    
    def setThoroughbred(self, thoroughbred):
        self.thoroughbred = thoroughbred
    
    def play(self):
        pass
    
    def __str__(self):
        return "id: {}\nName: {}\nРожден: {}\nПородистый: {}\n".format(self.getId(), self.getName(), self.getBirthdate(), self.thoroughbred)
