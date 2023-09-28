class Animal:
    def __init__(self, id, name, birthdate):
        self.id = id
        self.name = name
        self.birthdate = birthdate

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_birthdate(self):
        return self.birthdate

    def set_birthdate(self, birthdate):
        self.birthdate = birthdate

    def feed(self):
        print(self.name + " сыт.")

    def __str__(self):
        return "id: {}\nName: {}\nРожден: {}\n".format(self.id, self.name, self.birthdate)