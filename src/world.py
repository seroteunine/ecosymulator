import random
from animal import Animal, FemaleAnimal, MaleAnimal
from gridcell import GridCell

class World:
    def __init__(self, amount: int, dimension: (int, int)):
        self.X = dimension[0]
        self.Y = dimension[1]
        self.grid = [[GridCell(x, y) for x in range(self.X)] for y in range(self.Y)]
        self.__initialize_animals(amount)
        
    def __initialize_animals(self, amount: int):
        for _ in range(amount):
            animal_class = random.choice([FemaleAnimal, MaleAnimal])
            animal: Animal = animal_class()
            x, y = random.randint(0, self.X - 1), random.randint(0, self.Y - 1)
            self.grid[y][x].add_animal(animal)

    def update_simulation(self):
        for y in range(self.Y):
            for x in range(self.X):
                print(self.grid[y][x].animals)

    def draw_world(self):
        for animal in self.animals:
            print(animal.position, animal.age_days)