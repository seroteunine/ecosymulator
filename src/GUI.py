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
        self.WIDTH_CELL = self.WIDTH_SCREEN / self.world.X
        self.HEIGHT_CELL =  self.HEIGHT_SCREEN / self.world.Y

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
        return True 

    def refresh(self):
        self.screen.fill("white")

        for y in range(self.world.Y):
            for x in range(self.world.X):
                for animal in self.world.grid[y][x].animals:
                    position = (x * self.WIDTH_CELL, y * self.HEIGHT_CELL)

                    rect = pygame.Rect(position, (self.WIDTH_CELL, self.HEIGHT_CELL))
                    color = 'blue' if animal.gender == Gender.MALE else 'pink'
                    pygame.draw.rect(self.screen, color, rect, 20)

                    font = pygame.font.Font('freesansbold.ttf', 14)
                    text_content = str(animal.age_days)
                    text = font.render(text_content, True, 'black')
                    textRect = text.get_rect()
                    textRect.center = position
                    self.screen.blit(text, textRect)

        pygame.display.flip()
