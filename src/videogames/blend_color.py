import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen_size = (640, 480)
screen = pygame.display.set_mode(screen_size, 0, 32)

color1 = (221, 99, 20)
color2 = (96, 130, 51)
factor = 0.

def lerp(value1, value2, factor):
    return value1 + (value2 - value1) * factor

def blend_color(color1, color2, blend_factor):
    red1, green1, blue1 = color1
    red2, green2, blue2 = color2
    red = lerp(red1, red2, blend_factor)
    green = lerp(green1, green2, blend_factor)
    blue = lerp(blue1, blue2, blend_factor)
    return int(red), int(green), int(blue)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    tri = [ (0,120), (639,100), (639, 140) ]
    pygame.draw.polygon(screen, (0,255,0), tri)
    pygame.draw.circle(screen, (0,0,0), (int(factor*639.), 120), 10)

    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        factor = x / screen_size[0]
        pygame.display.set_caption(f"Factor {factor:.3f} Color {color}")

    color = blend_color(color1, color2, factor)
    pygame.draw.rect(screen, color, (0, 240, screen_size[0], 240))

    pygame.display.update()

pygame.quit()
