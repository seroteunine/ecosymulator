from enum import Enum
import random

from events import Event, EventEnum

class Gender(Enum):
    MALE = 'MALE',
    FEMALE = 'FEMALE'

class Animal:
    def __init__(self, X, Y, x, y, event_queue, get_neighbours_callback):
        self.max_X_world, self.max_Y_world = X, Y
        self.x, self.y = x, y
        self.event_queue = event_queue
        self.get_neighbours = get_neighbours_callback
        self.age_days = 0
        self.MAXIMUM_AGE = 5475

    def do_move(self):
        self.__walk_random()
        self.__get_older()
        self.__emit_die_when_old()

    def __walk_random(self):
        dir_x, dir_y = random.choice([-1,0,1]), random.choice([-1,0,1])
        self.x = max(0, min(self.x + dir_x, self.max_X_world - 1))
        self.y = max(0, min(self.y + dir_y, self.max_Y_world - 1))

    def __get_older(self, day: int = 1):
        self.age_days += day

    def __emit_die_when_old(self):
        if self.age_days >= self.MAXIMUM_AGE:
            event: Event = Event(EventEnum.DIE, self)
            self.event_queue.add_event(event)

class FemaleAnimal(Animal):
    def __init__(self, X, Y, x, y, event_queue, get_neighbours_callback):
        super().__init__(X, Y, x, y, event_queue, get_neighbours_callback)
        self.gender = Gender.FEMALE
        self.PREGNANCY_DURATION_DAYS = 147
        self.is_pregnant = False
        self.day_start_pregnancy = None

    def do_move(self):
        if self.is_pregnant and (self.age_days - self.day_start_pregnancy) >= self.PREGNANCY_DURATION_DAYS:
            self.__emit_create_child(self.x, self.y)
            self.is_pregnant = False
            self.day_start_pregnancy = None
        return super().do_move()
    
    def __emit_create_child(self, x, y):
        event: Event = Event(EventEnum.CREATE_CHILD, (x, y))
        self.event_queue.add_event(event)

    def get_impregnated(self):
        if self.age_days > 90 and not self.is_pregnant:
            self.is_pregnant = True
            self.day_start_pregnancy = self.age_days

class MaleAnimal(Animal):
    def __init__(self, X, Y, x, y, event_queue, get_neighbours_callback):
        super().__init__(X, Y, x, y, event_queue, get_neighbours_callback)
        self.gender = Gender.MALE
        self.fertility = 1 #Probability of successfull impregnation

    def do_move(self):
        self.try_impregnate_neighbours()
        return super().do_move()

    def try_impregnate_neighbours(self):
        neighbours = self.get_neighbours(self)
        for neighbour in neighbours:
            if neighbour.gender == Gender.FEMALE:
                if random.random() <= self.fertility:
                    neighbour.get_impregnated()