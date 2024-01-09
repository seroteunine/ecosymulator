import random


class Animal:
    def __init__(self, dimension_world: (int, int)):
        self.age_days = 0
        self.position = (random.randint(0, dimension_world[0]), random.randint(0, dimension_world[1]))

    def add_age_day(self, day: int = 1):
        self.age_days += day

    def make_move(self):
        self.__walk_random()

    def __walk_random(self):
        dir_x, dir_y = random.choice([-1,0,1]), random.choice([-1,0,1])
        self.position = (self.position[0] + dir_x, self.position[1] + dir_y)