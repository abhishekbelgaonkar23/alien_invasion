import pygame

class ship:
	def __init__(self, ai_game):
		self.screen = ai.game_screen
		self.screen_rect = ai_game.screen.get_rect()
		
		# load the ships image
		self.image = pygame.image.load(images/ship.bmp)
		self.rect = self.image.get_rect()
		
		self.rect.midbottom = self.screen_rect.midbottom # start each new ship at the bottom center of the screen
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
