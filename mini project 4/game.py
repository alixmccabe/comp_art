import pygame
import pygame.locals
import sys

def move_objects(x,y):
	
	screen = pygame.display.set_mode((640,480))
	screen.fill((255, 255, 255))
	pygame.init()

	while (True):

	   # check for quit events
	   for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	             pygame.quit(); sys.exit();

	   # draw the updated picture
	   pygame.draw.rect(screen, (0,255,0), (x,y,10,5), 50)

	   # update the screen
	   pygame.display.update()

move_objects(320,240)