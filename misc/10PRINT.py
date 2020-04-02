from random import random
import pygame


WIDTH, HEIGHT = (800, 800)
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()

pygame.display.set_caption("10PRINT")
window = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

sqaure_size = 10

def draw():
    window.fill(black)

    for x in range(0, WIDTH, sqaure_size):
        for y in range(0, HEIGHT, sqaure_size):
            if random() > .5:
                pygame.draw.line(window, white, (x, y), (x + sqaure_size, y +sqaure_size))
            else:
                pygame.draw.line(window, white, (x, y + sqaure_size), (x + sqaure_size, y))

while running:
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        draw()
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # updating the display        
    pygame.display.flip()