import pygame
from animal import Gender

from world import World

class GUI:
    WIDTH_SCREEN = 1280
    HEIGHT_SCREEN = 720

    def __init__(self, world: World):
        self.world = world
        self.initialize()

    def initialize(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH_SCREEN, self.HEIGHT_SCREEN))
        self.WIDTH_AGENT = self.WIDTH_SCREEN / self.world.grid_dimension[0]
        self.HEIGHT_AGENT =  self.HEIGHT_SCREEN / self.world.grid_dimension[1]

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
        return True 

    def refresh(self):
        self.screen.fill("white")

        for animal in self.world.animals:
            position = (animal.position[0] * self.WIDTH_AGENT, animal.position[1] * self.HEIGHT_AGENT)

            rect = pygame.Rect(position, (self.WIDTH_AGENT, self.HEIGHT_AGENT))
            color = 'blue' if animal.gender == Gender.MALE else 'pink'
            pygame.draw.rect(self.screen, color, rect, 20)

            font = pygame.font.Font('freesansbold.ttf', 14)
            text_content = str(animal.age_days)
            text = font.render(text_content, True, 'black')
            textRect = text.get_rect()
            textRect.center = position
            self.screen.blit(text, textRect)

        pygame.display.flip()
