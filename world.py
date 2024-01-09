from animal import Animal

class World:
    def __init__(self, amount: int, dimension: (int, int)):
        self.grid_dimension = dimension
        self.animals = []
        self.__initialize_animals(amount)
        
    def __initialize_animals(self, amount: int):
        for _ in range(amount):
            animal: Animal = Animal(self.grid_dimension)
            self.animals.append(animal)

    def update_simulation(self):
        for animal in self.animals:
            animal.make_move()
            animal.add_age_day()

    def draw_world(self):
        for animal in self.animals:
            print(animal.position, animal.age_days)