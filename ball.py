import pygame
import sys

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Red Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


radius = 25
x, y = width // 2, height // 2
speed = 20

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_d] and x + radius + speed <= width:
        x += speed
    if keys[pygame.K_w] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_s] and y + radius + speed <= height:
        y += speed

    clock.tick(60)

pygame.quit()
sys.exit()
