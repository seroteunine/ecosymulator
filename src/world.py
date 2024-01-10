import random
from animal import Animal, FemaleAnimal, Gender, MaleAnimal

class World:
    def __init__(self, amount: int, dimension: (int, int)):
        self.X = dimension[0]
        self.Y = dimension[1]
        self.animals = set()
        self.__initialize_animals(amount)
        
    def __initialize_animals(self, amount: int):
        for _ in range(amount):
            animal_class = random.choice([FemaleAnimal, MaleAnimal])
            animal: Animal = animal_class(self.X, self.Y)
            self.animals.add(animal)

    def update_simulation(self):
        for animal in self.animals:
            animal.do_move()

    def draw_world(self):
        for animal in self.animals:
            print(animal.position, animal.age_days)