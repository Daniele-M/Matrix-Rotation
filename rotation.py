import pygame as pg
import numpy as np
from os import sys
from settings import *
from support import *

pg.init()
class Rotation:
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.FramePerSec = pg.time.Clock()
        self.angle = 0
        self.dimension = 3
        self.vertex_count = 5
        self.in_menu = False
        self.setup()
        self.loop()
        
    def loop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False 
            self.screen.fill("black")
            
            if self.in_menu:
                draw_menu(self.screen)
            else:
                self.rotate()
                self.angle += 0.01
            pg.display.update()
            self.FramePerSec.tick(FPS)
        

    def setup(self):
        if self.dimension == 2:
            self.center = [WIDTH//2, HEIGHT//2]
            self.radius = WIDTH//4
            self.points = create_2Dpolygon(self.vertex_count, WIDTH//4)

        if self.dimension == 3:
            self.center = [WIDTH//2, HEIGHT//2, 0]
            self.points = createCube(self.center)
            self.proj_matrix = np.array([
                            [np.sqrt(3), 0, -np.sqrt(3)],
                            [1, 2, 1],
                            [np.sqrt(2), -np.sqrt(2), np.sqrt(2)]
                            ]) * (1/np.sqrt(6))

    def rotate(self):
        if self.dimension == 3:
            [rot_matrix_x, rot_matrix_y, rot_matrix_z] = create3DrotationMatrix(self.angle)
            rotate3D(self.screen, self.points, self.center, rot_matrix_z, self.proj_matrix)
        if self.dimension == 2:
            rot_matrix = np.array([[np.cos(self.angle), np.sin(self.angle)],
                                   [-np.sin(self.angle), np.cos(self.angle)]])
            rotate2D(self.screen, self.points, self.center, rot_matrix)


r = Rotation()
pg.quit()
    

