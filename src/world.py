import random
from animal import Animal, FemaleAnimal, MaleAnimal

class World:
    def __init__(self, amount: int, dimension: (int, int)):
        self.grid_dimension = dimension
        self.animals = []
        self.__initialize_animals(amount)
        
    def __initialize_animals(self, amount: int):
        for _ in range(amount):
            animal_class = random.choice([FemaleAnimal, MaleAnimal])
            animal: Animal = animal_class(self.grid_dimension)
            self.animals.append(animal)

    def update_simulation(self):
        for animal in self.animals:
            animal.make_move()
        self.__to_next_day()

    def __to_next_day(self):
        for animal in self.animals:
            animal.get_older()

    def draw_world(self):
        for animal in self.animals:
            print(animal.position, animal.age_days)