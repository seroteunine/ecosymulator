import pygame
from animal import Gender

from world import World

class GUI:
    WIDTH_SCREEN = 1280
    HEIGHT_SCREEN = 720
    MALE_COLOR = 'blue'
    FEMALE_COLOR = 'pink'
    GRASS_COLOR = pygame.Color(144, 238, 144)
    WATER_COLOR = pygame.Color(0, 191, 255)

    def __init__(self, world: World):
        self.world = world
        self.initialize()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN))
        self.WIDTH_CELL = self.WIDTH_SCREEN / self.world.X
        self.HEIGHT_CELL =  self.HEIGHT_SCREEN / self.world.Y

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
        return True 

    def refresh(self):
        #Render land
        self.screen.fill(self.GRASS_COLOR)

        #Render water
        for x, y in self.world.water_map:
            position = (x * self.WIDTH_CELL, y * self.HEIGHT_CELL)
            rect = pygame.Rect(position, (self.WIDTH_CELL, self.HEIGHT_CELL))
            pygame.draw.rect(self.screen, self.WATER_COLOR, rect)

        #Render animals
        for animal in self.world.animals:
            position = (animal.x * self.WIDTH_CELL, animal.y * self.HEIGHT_CELL)

            rect = pygame.Rect(position, (self.WIDTH_CELL, self.HEIGHT_CELL))
            color = self.MALE_COLOR if animal.gender == Gender.MALE else self.FEMALE_COLOR
            pygame.draw.rect(self.screen, color, rect)

            font = pygame.font.Font('freesansbold.ttf', 14)
            text_content = str(animal.age_days)
            text = font.render(text_content, True, 'black')
            textRect = text.get_rect()
            textRect.center = position
            self.screen.blit(text, textRect)

        pygame.display.flip()
