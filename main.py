import pygame
import numpy as np
from numpy import random


def dist(pointA, pointB):
    return np.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)

def near_points(point):
    count = random.randint(2, 5)
    points_array = []
    for i in range(count):
        x = random.randint(-20, 20)
        y = random.randint(-20, 20)
        points_array.append((point[0] + x, point[1] + y))
    return points_array


if __name__ == '__main__':
    HEIGHT = 400
    pygame.init()
    screen = pygame.display.set_mode((600, HEIGHT))
    screen.fill(color="#FFFFFF")
    pygame.display.update()
    is_active = True
    is_pressed = False
    points = []
    count_of_keyup = 0
    clusters = {}
    while (is_active):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_pressed = True
                if event.button == 1:
                    is_pressed = True
                    coord = event.pos
                    points.append(coord)
                    pygame.draw.circle(screen, color='black', center=coord, radius=5)
            if event.type == pygame.MOUSEBUTTONUP:
                is_pressed = False
            if event.type == pygame.MOUSEMOTION:
                if is_pressed:
                    # if random.choice((0,10))==0:
                    # coord = event.pos
                    # pygame.draw.circle(screen, color='black', center=coord, radius=10)
                    if dist(event.pos, points[-1]) > 20:
                        coord = event.pos
                        pygame.draw.circle(screen, color='black', center=coord, radius=5)
                        for nearP in near_points(coord):
                            pygame.draw.circle(screen, color='black', center=nearP, radius=5)
                            points.append(nearP)
                        points.append(coord)
            if event.type == pygame.KEYUP:
                if event.key == 13:
                    count_of_keyup = count_of_keyup + 1
                    #if count_of_keyup == 1:
                    #    clusters = dbscan(points, 50, 4, screen)
                    #else:
                    #    for colour, points in zip(cycle(["blue", "green", "red", "yellow", "grey", "black"]),
                    #                              clusters.values()):
                    #        points_in_one_group = [p for p in points]
                    #        for p in points_in_one_group:
                    #            pygame.draw.circle(screen, color=colour, center=p, radius=5)

        pygame.display.update()
