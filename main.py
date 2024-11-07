import pygame as pg
import numpy as np
from os import sys
from support import *
from button import *

pg.init()
class Rotation:
    def __init__(self):
        self.running = True
        self.width = 600
        self.height = 600
        self.FPS = 60
        self.screen = pg.display.set_mode((self.width, self.height))
        self.FramePerSec = pg.time.Clock()
        self.angle = 0
        self.dimension = 2
        self.vertex_count = 5
        self.change_vertex = 0
        self.axis3d = np.array([1, 0, 0])
        self.in_menu = True
        self.is_mouse_released = False
        self.setup_menu()
        self.loop()
        
    def loop(self):
        while self.running:
            self.is_mouse_released = False
            self.get_events()
            self.screen.fill("black")
            
            if self.in_menu:
                self.angle = 0
                self.b2D.update()
                self.b3D.update()
                self.b2D.draw()
                self.b3D.draw()
            else:
                self.bback.update()
                self.bback.draw()
                self.rotation_options()
                self.rotate()
                self.angle += 0.01
            self.draw()
            self.FramePerSec.tick(self.FPS)   

    def get_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False 
            if event.type == pg.MOUSEBUTTONUP:
                self.is_mouse_released = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.change_vertex = -1
                if event.key == pg.K_RIGHT:
                    self.change_vertex = 1

    def setup_menu(self):
        self.b2D = Button2D(self, 50, 100, 200, 50, (86, 86, 86), "2D")
        self.b3D = Button3D(self, self.width-250, 100, 200, 50, (86, 86, 86), "3D")
        self.bback = ButtonBack(self, self.width-80, 50, 50, 50, (86, 86, 86), "<-")

    def setup(self):
        if self.dimension == 2:
            self.center = [self.width//2, self.height//2]
            self.radius = self.width//4
            self.points = create_2Dpolygon(self.vertex_count, self.width//4, self.width, self.height)

        if self.dimension == 3:
            self.center = [self.width//2, self.height//2, 0]
            self.points = createCube(self.center, self.width)
            self.proj_matrix = np.array([
                            [np.sqrt(3), 0, -np.sqrt(3)],
                            [1, 2, 1],
                            [np.sqrt(2), -np.sqrt(2), np.sqrt(2)]
                            ]) * (1/np.sqrt(6))

    def rotate(self):
        if self.dimension == 3:
            [rot_matrix_x, rot_matrix_y, rot_matrix_z] = create3DrotationMatrix(self.angle, self.axis3d)
            rotate3D(self.screen, self.points, self.center, rot_matrix_x @ rot_matrix_y @ rot_matrix_z,
                     self.proj_matrix, self.width, self.height)
        if self.dimension == 2:
            rot_matrix = np.array([[np.cos(self.angle), np.sin(self.angle)],
                                   [-np.sin(self.angle), np.cos(self.angle)]])
            rotate2D(self.screen, self.points, self.center, rot_matrix)

    def rotation_options(self):
        if self.dimension == 2:
            text = "Number of vertices: " + str(self.vertex_count)
            font = pg.font.SysFont("comicsans", 40)
            text = font.render(text, 1, (200, 200, 200))
            self.screen.blit(text, (self.width//2 - text.get_width()/2, self.height - 50))
            if self.change_vertex != 0:    
                self.vertex_count += self.change_vertex
                if self.vertex_count < 2:
                    self.vertex_count = 2
                self.change_vertex = 0
                self.setup()
        if self.dimension == 3:
            bx = Button3Dax(self, self.width//4 - 25, self.height - 75,
                            50, 50, (86, 86, 86), "x", "x")
            by = Button3Dax(self, self.width//2 - 25, self.height - 75,
                            50, 50, (86, 86, 86), "y", "y")
            bz = Button3Dax(self, 3*self.width//4 - 25, self.height - 75,
                            50, 50, (86, 86, 86), "z", "z")
            bx.update()
            by.update()
            bz.update()
            bx.draw()
            by.draw()
            bz.draw()
    
    def draw(self):
        pg.display.update()

r = Rotation()
pg.quit()
    

