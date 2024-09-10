import sys
import pygame
from settings import settings

class AlienInvasion:  # class to manage game assets and behavior
    def __init__(self): 
        pygame.init()
        self.settings = settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        while True:  # main loop
            for event in pygame.event.get():  # watch for keyboard & mouse events
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()  # make the most recently drawn screen visible

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

