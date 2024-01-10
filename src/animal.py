from enum import Enum
import random

class Gender(Enum):
    MALE = 'MALE',
    FEMALE = 'FEMALE'

class Animal:
    def __init__(self, X, Y):
        self.age_days = 0
        self.max_X_world = X
        self.max_Y_world = Y
        self.x = random.randint(0, X - 1)
        self.y = random.randint(0, Y - 1)

    def get_older(self, day: int = 1):
        self.age_days += day

    def do_move(self):
        self.__walk_random()
        print(self.__get_neighbours())

    def __walk_random(self):
        dir_x, dir_y = random.choice([-1,0,1]), random.choice([-1,0,1])
        self.x = max(0, min(self.x + dir_x, self.max_X_world - 1))
        self.y = max(0, min(self.y + dir_y, self.max_Y_world - 1))

    def __get_neighbours(self, distance: int = 1):
        pass

class FemaleAnimal(Animal):
    def __init__(self, X, Y):
        super().__init__(X, Y)
        self.gender = Gender.FEMALE

    def get_pregnant(self):
        print('Waddup im pregnant')

class MaleAnimal(Animal):
    def __init__(self, X, Y):
        super().__init__(X, Y)
        self.gender = Gender.MALE