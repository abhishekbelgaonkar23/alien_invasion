import sys
import pygame

class AlienInvasion: # overall class to manage game assets and behavior
	def __init__(self): 
		pygame.init()
		self.screen = pygame.display.set_mode(1200, 800)
		pygame.display.set_caption("Alien Invasion")
		
	def run_game(self):
		while True: # main loop for the game
			for event.type in pygame.event.get(): # watch for keyboard and mouse events
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip() # make the most recently drawn screen visible
if __name__ == '__main__': # make a game instance, and run the game
	
