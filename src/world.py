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
        self.__move_animals()
        self.__next_day()

    def __move_animals(self):
        for y in range(self.Y):
            for x in range(self.X):
                old_cell = self.grid[y][x]
                for animal in old_cell.animals:
                    dx, dy = random.randint(-1, 1), random.randint(-1, 1)
                    new_x, new_y = max(0, min(self.X - 1, x + dx)), max(0, min(self.Y - 1, y + dy))
                    new_cell = self.grid[new_y][new_x]
                    old_cell.remove_animal(animal)
                    new_cell.add_animal(animal)

    def __next_day(self):
        for y in range(self.Y):
            for x in range(self.X):
                cell = self.grid[y][x]
                for animal in cell.animals:
                    animal.get_older()

    def draw_world(self):
        for animal in self.animals:
            print(animal.position, animal.age_days)