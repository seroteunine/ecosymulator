from enum import Enum
import random

from events import Event, EventEnum

class Gender(Enum):
    MALE = 'MALE',
    FEMALE = 'FEMALE'

class Animal:
    def __init__(self, X, Y, x, y, event_queue, get_neighbours_callback, water_map):
        self.max_X_world, self.max_Y_world = X, Y
        self.x, self.y = x, y
        self.event_queue = event_queue
        self.get_neighbours = get_neighbours_callback
        self.water_map = water_map
        self.age_hours = 0
        self.last_day_drank_water = 0
        self.MAXIMUM_AGE = 1000 #5475 is realistic age in days of sheep
        self.MAXIMUM__SURVIVABLE_DAYS_WITHOUT_WATER = 10

    def do_move(self):
        self.__try_drink_water()
        self.__walk_random()
        self.__get_older()
        self.__try_dying()

    def __try_drink_water(self):
        if (self.x, self.y) in self.water_map:
            self.last_day_drank_water = self.age_hours // 24

    def __walk_random(self):
        dir_x, dir_y = random.choice([-1,0,1]), random.choice([-1,0,1])
        self.x = max(0, min(self.x + dir_x, self.max_X_world - 1))
        self.y = max(0, min(self.y + dir_y, self.max_Y_world - 1))

    def __get_older(self, hours: int = 1):
        self.age_hours += hours

    def __try_dying(self):
        should_die = self.age_hours // 24 >= self.MAXIMUM_AGE or (self.age_hours // 24 - self.last_day_drank_water) >= self.MAXIMUM__SURVIVABLE_DAYS_WITHOUT_WATER
        if should_die:
            event: Event = Event(EventEnum.DIE, self)
            self.event_queue.add_event(event)

class FemaleAnimal(Animal):
    def __init__(self, X, Y, x, y, event_queue, get_neighbours_callback, water_map):
        super().__init__(X, Y, x, y, event_queue, get_neighbours_callback, water_map)
        self.gender = Gender.FEMALE
        self.PREGNANCY_DURATION_DAYS = 147 #Average pregnancy of sheep
        self.is_pregnant = False
        self.day_start_pregnancy = None

    def do_move(self):
        if self.is_pregnant and (self.age_hours // 24 - self.day_start_pregnancy) >= self.PREGNANCY_DURATION_DAYS:
            self.__emit_create_child(self.x, self.y)
            self.is_pregnant = False
            self.day_start_pregnancy = None
        return super().do_move()
    
    def __emit_create_child(self, x, y):
        event: Event = Event(EventEnum.CREATE_CHILD, (x, y))
        self.event_queue.add_event(event)

    def get_impregnated(self):
        if self.age_hours // 24 > 90 and not self.is_pregnant: #Sheep are fertile after 3 months 
            self.is_pregnant = True
            self.day_start_pregnancy = self.age_hours // 24

class MaleAnimal(Animal):
    def __init__(self, X, Y, x, y, event_queue, get_neighbours_callback, water_map):
        super().__init__(X, Y, x, y, event_queue, get_neighbours_callback, water_map)
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