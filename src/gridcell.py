from animal import Animal

class GridCell:
    def __init__(self, x, y):
        self.position = (x, y)
        self.animals = set()

    def add_animal(self, animal: Animal):
        self.animals.add(animal)

    def remove_animal(self, animal: Animal):
        if animal in self.animals:
            self.animals.remove(animal)
    