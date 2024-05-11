import sys
import pygame
import random

def change_color():
    return [random.randint(0,255) for _ in range (3)]

pygame.init()
win = pygame.display.set_mode([800,600], pygame.RESIZABLE)

color1 = [255,0,0]
while True:
    win.fill(color1)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                color1 = change_color()
                print(color1)
    pygame.display.update()