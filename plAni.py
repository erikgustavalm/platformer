import pygame

class Animate(object):
	def __init__(self, filepath, width=64, height=64):
	# Filepath is given and return a finnished surface converted into alpha channel
		self.image = pygame.image.load(filepath).convert_alpha()
		
	# The present frame is the part of the spritesheet that will be blitted to the screen
		self.presentFrame = 0
		
	# A list of all the frames existing within the spritesheet
		self.frames = []
		
	# Divides the sprite sheet into frames with the size given in the constructor(standard 64x64)
		self.divide_frame(width, height)
	
	# Categorize the frames
		self.l_still, self.r_still = 0, 0
		self.l_runStart, self.r_runStart = 0, 0
		self.l_runEnd, self.r_runEnd = 0, 8
		self.l_jumpStart, self.r_jumpStart = 0, 0
		self.l_jumpEnd, self.r_jumpEnd = 0, 0
		
		self.frame_naming()
	
	# speed factors
		self.frame_speed = 0
		self.cap = 0
		
	def divide_frame(self, width, height):
	# gives two integers of how many rows and columns the sheet exist of
		numofcols = self.image.get_width() / width
		numofrows = self.image.get_height() / height
	# Take the number of rows and cols and multiply them with the size to give a cropped rect
		for row in range(numofrows):
			for col in range(numofcols):
				self.frames.append(pygame.Rect(col * width, row * height, width, height))
		self.presentFrame = self.frames[0]
		
	def frame_naming(self):
		self.l_still = self.frames[29]
		self.r_still = self.frames[0]
		self.l_runStart = self.frames[28]
		self.r_runStart = self.frames[1]
		self.l_runEnd = self.frames[21]
		self.r_runEnd = self.frames[8]
		self.l_jumpStart = self.frames[1]
		self.r_jumpStart = self.frames[1]
		self.l_jumpEnd = self.frames[1]
		self.r_jumpEnd = self.frames[1]
		
	def draw(self, screen, x, y):
	# with the passing arguments the image is drawn to the screen
		screen.blit(self.image, (x, y), self.presentFrame)
	
	def animator(self, type):
		if type == "still/right":
			self.presentFrame = self.r_still
			self.frame_speed = 0
			self.cap = 0
				
		if type == "still/left":
			self.presentFrame = self.l_still
			self.frame_speed = 0
			self.cap = 0
			
		if type == "run/right":
			self.frame_speed += 1
			if self.cap == 0:
				self.cap = 1
			if self.frame_speed == 3:	
				self.presentFrame = self.frames[self.cap]
				self.frame_speed = 0
				self.cap += 1
				if self.cap > 8:
					self.cap = 1
				
		if type == "run/left":
			self.frame_speed +=1
			if self.cap < 21 or  self.cap > 28:
				self.cap = 28
			if self.frame_speed == 3:
				self.presentFrame = self.frames[self.cap]
				self.frame_speed = 0
				self.cap -= 1
				if self.cap < 21:
					self.cap = 28
					
		if type == "jump/right":
			self.frame_speed +=1
			
			if self.frame_speed == 3:
				self.presentFrame = self.frames[self.cap]
				self.frame_speed = 0
				self.cap += 1
				if self.cap > self.r_jumpEnd:
					self.cap = r_jumpEnd
			
		if type == "jump/left":
			self.frame_speed +=1
			
			if self.frame_speed == 3:
				self.presentFrame = self.frames[self.cap]
				self.frame_speed = 0
				self.cap += 1
				if self.cap < self.l_jumpEnd:
					self.cap = self.l_jumpEnd

