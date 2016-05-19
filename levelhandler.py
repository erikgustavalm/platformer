import pygame

class Levelhandler(object):
	def __init__(self):
		self.menu = False
		self.level1 = False
		self.loaded = False
		
		self.background = 0
		self.objects = []
	
	def update(self, screen):
		if not self.loaded:
			if self.menu:
				self.background = (100,100,100)
				self.objects = []
				self.loadScene("menu")
				self.loaded = True
				
		if not self.loaded:
			if self.level1:
				self.background = (100,100,255)
				self.objects = []
				self.loadScene("level1")
				self.loaded = True

		if self.loaded:
			screen.fill(self.background)
			for obj in self.objects:
				obj.update(screen)

			
			
	def loadScene(self, scene):
		if scene == "menu":
			pass

		if scene == "level1":
			box = static_object("box.png", 30, 30)
			self.objects.append(box)

class static_object(object):
	def __init__(self, filepath, x, y):
		self.image = pygame.image.load(filepath).convert_alpha()
		self.ypos = y
		self.xpos = x

	def update(self, screen):
		screen.blit(self.image, (self.xpos, self.ypos))
