import pygame 	
from player import *

pygame.init()
jstick = pygame.joystick.Joystick(0)
jstick.init()
print jstick.get_name()

SCREEN_DIM = (1240,960)

screen = pygame.display.set_mode(SCREEN_DIM, 0, 32)

#Loading all the right things
player1 = Player("george.png")


FPS_CLOCK = pygame.time.Clock()
FPS = 30
running = True

while running:
	FPS_CLOCK.tick()
	screen.fill((255,255,255))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			
			if event.key == pygame.K_RIGHT:
				player1.move_left = False
				player1.move_right = True
				player1.stand_still = False

			if event.key == pygame.K_LEFT:
				player1.move_left = True
				player1.move_right = False
				player1.stand_still = False

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				player1.move_right = False
				player1.stand_still = True

			if event.key == pygame.K_LEFT:
				player1.move_left = False
				player1.stand_still = True

		if event.type == pygame.JOYAXISMOTION:
			
		# X-Axis
			if event.axis == 0: 
		
			#Player goes Left joystick
				if event.value < 0:
					player1.move_left = True
					player1.move_right = False
					player1.stand_still = False
			
			#Player goes Right joystick
				elif event.value > 0:
					player1.move_right = True
					player1.move_left = False
					player1.stand_still = False

			#If the player stands still joystick
				if event.value == 0:
					player1.move_left, player1.move_right = False, False
					player1.stand_still = True
	
		if event.type == pygame.JOYBUTTONDOWN:
			print event.button
			if event.button == 3:
				running = False
			if event.button == 1:
				player1.x = 130
			if event.button == 5:
				player1.idle = True 
			if event.button == 4:
				if player1.zoom:
					player1.zoom = False
				else:
					player1.zoom = True
#Update Screen related objects
	player1.update(screen)

	pygame.display.update()
	FPS_CLOCK.tick(FPS)

pygame.quit()
