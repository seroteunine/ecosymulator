import random
from animal import FemaleAnimal, MaleAnimal
from events import Event, EventEnum, EventQueue

class World:
    def __init__(self, amount: int, dimension: (int, int)):
        self.X = dimension[0]
        self.Y = dimension[1]
        self.event_queue = EventQueue()
        self.water_map = set()
        self.animals = set()
        self.__initialize_animals(amount)
        self.__initialize_water(10)

    def update_simulation(self):
        for animal in set(self.animals): #Use copy so that its size is not changed during iteration
            animal.do_move()
        for event in self.event_queue.get_event():
            self.handle_event(event)

    def handle_event(self, event: Event):
        if event.type == EventEnum.CREATE_CHILD:
            self.add_animal(*event.data)
        elif event.type == EventEnum.DIE:
            self.animals.remove(event.data)
        
    def __initialize_animals(self, amount: int):
        for _ in range(amount):
            self.add_animal_random()

    def __initialize_water(self, amount: int):
        for _ in range(amount):
            x, y = random.randint(0, self.X - 1), random.randint(0, self.Y - 1)
            self.water_map.add((x, y))

    def add_animal_random(self):
        x, y = random.randint(0, self.X - 1), random.randint(0, self.Y - 1)
        self.add_animal(x, y)

    def add_animal(self, x, y):
        animal_class = random.choice([FemaleAnimal, MaleAnimal])
        animal = animal_class(
            self.X, self.Y, 
            x, y,
            self.event_queue,
            self.get_neighbours
        )
        self.animals.add(animal)

    def get_neighbours(self, animal, distance: int = 1):
        neighbours = set()
        for other_animal in self.animals:
            if animal != other_animal and self.__calculate_distance(animal, other_animal) <= distance:
                neighbours.add(other_animal)
        return neighbours
    
    def __calculate_distance(self, animal, other_animal): # Uses Chebyshev distance
        return max(abs(other_animal.y - animal.y), abs(other_animal.x - animal.x))