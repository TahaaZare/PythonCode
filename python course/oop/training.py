class Animal:
    def __init__(self, animalName):
        self.AnimalName = animalName

    def showAnimalName(self):
        print(f'Animal Name is : {self.AnimalName}')

dog = Animal('dog')
print(dog.showAnimalName())