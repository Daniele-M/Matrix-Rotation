import pygame as pg
import numpy as np
from os import sys
from settings import *
from support import *


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
FramePerSec = pg.time.Clock()

dimension = 3
theta = 0.0


if dimension == 2:
    center = [WIDTH//2, HEIGHT//2]
    radius = WIDTH//4
    vertex_count = 6

    points = create_2Dpolygon(vertex_count, WIDTH//4)
    rot_matrix = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])

if dimension == 3:
    center = [WIDTH//2, HEIGHT//2, 0]
    points = createCube(center)
    proj_matrix = np.array([
                            [np.sqrt(3), 0, -np.sqrt(3)],
                            [1, 2, 1],
                            [np.sqrt(2), -np.sqrt(2), np.sqrt(2)]
                            ]) * (1/np.sqrt(6))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit() 
    screen.fill("black")
    
    if dimension == 3:
        [rot_matrix_x, rot_matrix_y, rot_matrix_z] = create3DrotationMatrix(theta)
        rotate3D(screen, points, center, rot_matrix_z, proj_matrix)
    if dimension == 2:
        rot_matrix = np.array([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        rotate2D(screen, points, center, rot_matrix)

    theta += 0.01
    pg.display.update()
    FramePerSec.tick(FPS)
    

