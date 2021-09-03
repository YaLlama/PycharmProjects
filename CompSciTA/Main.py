import pygame
import displayControler2
import ObjectControl
import Display
import time

background_colour = (255,255,255)
(width, height) = (900, 700)
forestGreen = (34, 139, 34)

pygame.init()
clock = pygame.time.Clock()
display = displayControler2.display(pygame.display, width, height)
shapes = ObjectControl.objectControl(display)


running = True



count = 2

while running:

    shapes.regularShape(width/2, height/2, 200, count, (0, 0, 210))
    display.update()
    count += 1
    clock.tick(30)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
