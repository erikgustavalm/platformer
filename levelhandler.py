import pygame
from objectHandler import*

class Levelhandler(object):
	def __init__(self):
		self.menu = False
		self.level1 = False
		self.loaded = False
		
		self.obHandler = objectHandler()

		self.background = 0
		self.objects = []

	def update(self, screen):
		if not self.loaded:
			if self.menu:
				self.background = pygame.image.load("levels/menu.png")
				self.objects = []
				self.objects = self.obHandler.import_objects("menu")
				self.loaded = True
				
		if not self.loaded:
			if self.level1:
				self.background = pygame.image.load("levels/level1.png")
				self.objects = []
				self.objects = self.obHandler.import_objects("level1")
				self.loaded = True

		if self.loaded:
			#for obj in self.objects:
			#	obj.update(screen)

			screen.blit(self.background, (0,0))
			
	
