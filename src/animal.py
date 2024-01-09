from enum import Enum
import random

class Gender(Enum):
    MALE = 'MALE',
    FEMALE = 'FEMALE'

class Animal:
    def __init__(self):
        self.age_days = 0

    def get_older(self, day: int = 1):
        self.age_days += day

    def make_move(self):
        self.__walk_random()

    def __walk_random(self):
        dir_x, dir_y = random.choice([-1,0,1]), random.choice([-1,0,1])
        new_x = max(0, min(self.position[0] + dir_x, self.dimension_world[0] - 1))
        new_y = max(0, min(self.position[1] + dir_y, self.dimension_world[1] - 1))
        self.position = (new_x, new_y)

class FemaleAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.gender = Gender.FEMALE

class MaleAnimal(Animal):
    def __init__(self):
        super().__init__()
        self.gender = Gender.MALE