import pygame 	
from player import*
from levelhandler import*

pygame.init()
jstick = pygame.joystick.Joystick(0)
jstick.init()
print jstick.get_name()

SCREEN_DIM = (1240,960)

screen = pygame.display.set_mode(SCREEN_DIM, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE, 32)

#Loading all the right things
george = Player("george.png")
mapController = Levelhandler()
mapController.menu = True

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
				george.move_left = False
				george.move_right = True
				george.stand_still = False

			if event.key == pygame.K_LEFT:
				george.move_left = True
				george.move_right = False
				george.stand_still = False
				
			if event.key == pygame.K_UP:
				george.jump = True
				george.on_ground = False
				print "up"
	
			if event.key == pygame.K_RETURN:
				if mapController.menu:
					mapController.level1 = True
					mapController.menu = False
					mapController.loaded = False

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				george.move_right = False
				george.stand_still = True

			if event.key == pygame.K_LEFT:
				george.move_left = False
				george.stand_still = True
			
			if event.key == pygame.K_UP:
				george.jump = False
				george.on_ground = True

		if event.type == pygame.JOYAXISMOTION:
			
		# X-Axis
			if event.axis == 0: 
		
			#Player goes Left joystick
				if event.value < 0:
					george.move_left = True
					george.move_right = False
					george.stand_still = False
			
			#Player goes Right joystick
				elif event.value > 0:
					george.move_right = True
					george.move_left = False
					george.stand_still = False

			#If the player stands still joystick
				if event.value == 0:
					george.move_left, george.move_right = False, False
					george.stand_still = True
	
		if event.type == pygame.JOYBUTTONDOWN:
			print event.button
			if event.button == 3:
				running = False
			 
			
#Update Screen related objects
	mapController.update(screen)
	if not mapController.menu:
		george.update(screen)

	pygame.display.update()
	FPS_CLOCK.tick(FPS)

pygame.quit()
