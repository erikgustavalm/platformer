import pygame
from plAni import*

class Player():
	def __init__(self, filepath):
		self.sprite = Animate(filepath)
		self.xpos = 130
		self.ypos = 430
		self.move_left = False
		self.move_right = False
		self.stand_still = True
		self.idle = False
	
	def update(self, screen):		
		self.move()
		self.sprite.draw(screen, self.xpos, self.ypos)
				
	def move(self):
		if self.move_right:
			self.xpos += 5
			self.sprite.animator("run/right")

		if self.move_left:
			self.xpos -= 5
			self.sprite.animator("run/left")
					
		if self.stand_still:
			self.sprite.animator("stand/still")			
	
		
		
