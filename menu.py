class Menu:
    @staticmethod
    def showMainMenu():
        print("Введите цифру необходимого действия: \n" +
                "1. Показать весь питомник\n" +
                "2. Показать только выбранный вид животных\n" +
                "3. Увидеть список команд, выполняемых животным\n" +
                "4. Обучить животное новым командам\n" +
                "5. Завести новое животное")

    @staticmethod
    def printOnlyThisClass(animalFarm):
        print("Выберите вид животных: \n" +
                "1. Домашние\n" +
                "2. Вьючные")
        userSelectedClass = int(input())
        if userSelectedClass == 1:
            animalFarm.printOnlyThisClass(1)
        elif userSelectedClass == 2:
            animalFarm.printOnlyThisClass(2)

    @staticmethod
    def Comands():
        print("Выберите тип животных: \n" +
                "1. Домашние\n" +
                "2. Вьючные")
        userSelectedClass = int(input())
        userSelected = 0
        if userSelectedClass == 1:
            print("Выберите вид животных: \n" +
                "1. Кошки\n" +
                "2. Собаки\n")