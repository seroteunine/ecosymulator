from enum import Enum

class EventEnum(Enum):
    DIE = 'die',
    GET_NEIGHBOUR = 'get_neighbour',
    CREATE_CHILD = 'create_child'

class Event:
    def __init__(self, type: EventEnum, data = None):
        self.type = type
        self.data = data

class EventQueue:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def get_event(self):
        while self.events:
            yield self.events.pop(0)