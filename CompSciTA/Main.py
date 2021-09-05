import pygame
import displayControler2
import ObjectControl
import Display
import time

background_colour = (255,255,255)
(width, height) = (1600, 800)
forestGreen = (34, 139, 34)

pygame.init()
clock = pygame.time.Clock()
display = displayControler2.display(pygame.display, width, height)
shapes = ObjectControl.objectControl(display,width,height)


running = True

faces = [[[152, 147], [247, 147], [152, 52], [247, 52]], [[139, 160], [260, 160], [139, 39], [260, 39]], [[139, 160], [260, 160], [152, 147], [247, 147]], [[139, 39], [260, 39], [152, 52], [247, 52]], [[139, 160], [139, 39], [152, 147], [152, 52]], [[260, 160], [260, 39], [247, 147], [247, 52]]]

face1 = [[152, 147], [247, 147], [152, 52], [247, 52]]
face2 = [[139, 160], [260, 160], [139, 39], [260, 39]]
face3 = [[139, 160], [260, 160], [152, 147], [247, 147]]
face4 = [[139, 39], [260, 39], [152, 52], [247, 52]]
face5 = [[139, 160], [139, 39], [152, 147], [152, 52]]
face6 = [[260, 160], [260, 39], [247, 147], [247, 52]]



count = 2
shapes.regularShape(width/2, height/2, 200, count, (0, 0, 210))
display.update()
count += 1


camera = [0, 0, 0]



while running:

    shapes.cube(camera)
    display.update()

    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                camera[1] += 1
            if event.key == pygame.K_s:
                camera[1] -= 1
            if event.key == pygame.K_a:
                camera[0] -= 1
            if event.key == pygame.K_d:
                camera[0] += 1
            if event.key == pygame.K_q:
                camera[2] += 1
            if event.key == pygame.K_e:
                camera[2] -= 1

        if event.type == pygame.QUIT:
          running = False
