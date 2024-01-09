from animal import Animal

class GridCell:
    def __init__(self, x, y):
        self.position = (x, y)
        self.animals = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)

    def remove_animal(self, animal: Animal):
        for _animal in self.animals:
            if _animal == animal:
                self.animals.remove(animal)