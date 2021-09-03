import pygame
import Display
import ObjectControl


background_colour = (255,255,255)
(width, height) = (900, 700)
forestGreen = (34, 139, 34)

pygame.init()
clock = pygame.time.Clock()
display = Display.display(pygame.display, width, height)
shapes = ObjectControl.objectControl(display)


running = True



while running:


    shapes.regularShape(width/2, height/2, 200, 5, (0, 0, 210))
    display.update()
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False