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
		self.jump = False
		self.on_ground = True
		self.gravity = True
			
	def update(self, screen):		
		self.move()
		self.sprite.draw(screen, self.xpos, self.ypos)
				
	def move(self):
			
		if self.move_right:
			self.xpos += 5
			self.sprite.animator("run/right")
			print "right"

		if self.move_left:
			self.xpos -= 5
			self.sprite.animator("run/left")
			print "left"	
			
		if self.stand_still:
			self.sprite.animator("stand/still")	
		
		#If George is jumping right	
		if self.jump and self.move_right:
			self.xpos +=5
			self.ypos -=7
			self.sprite.animator("jump/right")

		#If George is jumping left
		if self.jump and self.move_left:
			self.xpos -=5
			self.ypos -=7
			self.sprite.animator("jump/left")
			
		#If George is jumping Up (idle)
		if self.jump and self.move_left == False and self.move_right == False:
			self.ypos -=7
		
		if self.ypos < 430 and self.jump ==False:
			self.ypos +=15