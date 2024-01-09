import pygame

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
        self.clock = pygame.time.Clock()
        self.running = True
        self.clock.tick(60)
        self.WIDTH_AGENT = self.WIDTH_SCREEN / self.world.grid_dimension[0]
        self.HEIGHT_AGENT =  self.HEIGHT_SCREEN / self.world.grid_dimension[1]

    def refresh(self):
        self.screen.fill("white")

        for animal in self.world.animals:
            rect = pygame.Rect((animal.position[0] * self.WIDTH_AGENT, animal.position[1] * self.HEIGHT_AGENT), (self.WIDTH_AGENT, self.HEIGHT_AGENT))
            pygame.draw.rect(self.screen, 'black', rect, 20)

        pygame.display.flip()
