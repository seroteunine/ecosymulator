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
            animal: Animal = animal_class(self.X, self.Y, self.get_neighbours)
            self.animals.add(animal)

    def update_simulation(self):
        for animal in self.animals:
            animal.do_move()

    def get_neighbours(self, animal, distance: int = 1):
        neighbours = set()
        for other_animal in self.animals:
            if animal != other_animal and self.__calculate_distance(animal, other_animal) <= distance:
                neighbours.add(other_animal)
        return neighbours
    
    def __calculate_distance(self, animal, other_animal):
        # Uses Chebyshev distance
        return max(abs(other_animal.y - animal.y), abs(other_animal.x - animal.x))