from enum import Enum
import random

class Gender(Enum):
    MALE = 'MALE',
    FEMALE = 'FEMALE'

class Animal:
    def __init__(self, X, Y, x, y, get_neighbours_callback):
        self.age_days = 0
        self.max_X_world = X
        self.max_Y_world = Y
        self.x = x
        self.y = y
        self.MAXIMUM_AGE = 5475
        self.get_neighbours = get_neighbours_callback

    def get_older(self, day: int = 1):
        self.age_days += day

    def do_move(self):
        self.__walk_random()
        self.get_older()

    def __walk_random(self):
        dir_x, dir_y = random.choice([-1,0,1]), random.choice([-1,0,1])
        self.x = max(0, min(self.x + dir_x, self.max_X_world - 1))
        self.y = max(0, min(self.y + dir_y, self.max_Y_world - 1))


class FemaleAnimal(Animal):
    def __init__(self, X, Y, x, y, get_neighbours_callback, add_animal_callback):
        super().__init__(X, Y, x, y, get_neighbours_callback)
        self.gender = Gender.FEMALE
        self.PREGNANCY_DURATION_DAYS = 147
        self.is_pregnant = False
        self.day_start_pregnancy = None
        self.create_child = add_animal_callback

    def do_move(self):
        if self.is_pregnant and (self.age_days - self.day_start_pregnancy) >= self.PREGNANCY_DURATION_DAYS:
            self.create_child(x = self.x, y = self.y)
            self.is_pregnant = False
            self.day_start_pregnancy = None
        return super().do_move()

    def get_impregnated(self):
        if self.age_days > 90 and not self.is_pregnant:
            self.is_pregnant = True
            self.day_start_pregnancy = self.age_days

class MaleAnimal(Animal):
    def __init__(self, X, Y, x, y, get_neighbours_callback, add_animal_callback):
        super().__init__(X, Y, x, y, get_neighbours_callback)
        self.gender = Gender.MALE
        self.fertility = 1 #Probability that when trying to impregnate, it succeeds

    def do_move(self):
        self.try_impregnate_neighbours()
        return super().do_move()

    def try_impregnate_neighbours(self):
        neighbours = self.get_neighbours(self)
        for neighbour in neighbours:
            if neighbour.gender == Gender.FEMALE:
                if random.random() <= self.fertility:
                    neighbour.get_impregnated()