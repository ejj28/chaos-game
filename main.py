import pygame
import random

verticesCount = 3
vertices = []
for i in range(0, verticesCount):
    vertices.append([random.randint(0,500), random.randint(0,500)])

point = [random.randint(0,500), random.randint(0,500)]

print(vertices)

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

screen.fill((0, 0, 0))
for i in vertices:
        screen.set_at((i[0], i[1]), (255,255,255))

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

    

    pygame.display.flip()

pygame.quit()