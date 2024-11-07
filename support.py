import pygame as pg
import numpy as np
from shapely.geometry import Polygon 
from settings import *


def draw_menu(screen, dimension):
    screen.fill("black")

#2D
def create_2Dpolygon(vertex_count, radius):
    n, r = vertex_count, radius
    x, y = WIDTH//2, HEIGHT//2
    return np.array([(x + r*np.cos(2*np.pi*i/n), y + r*np.sin(2*np.pi*i/n)) for i in range(n)])

def draw_2Dshape(screen, points, center):
    pg.draw.polygon(screen, "white", points, width=1)
    pg.draw.circle(screen, "red", center, 5)
    
def rotate_2Dshape(rot_matrix, points, center):
    points = points - center
    for i in range(len(points)):
        points[i] = rot_matrix @ points[i]
    return points + center
        
def rotate2D(screen, points, center, rot_matrix):
    rotated_points = rotate_2Dshape(rot_matrix, points, center)
    draw_2Dshape(screen, rotated_points, center)

# 3D
def createCube(center):
    a = np.array([-1, -1, -1])*(WIDTH//4) + center
    b = np.array([1, -1, -1])*(WIDTH//4) + center
    c = np.array([1, 1, -1])*(WIDTH//4) + center
    d = np.array([-1, 1, -1])*(WIDTH//4) + center
    e = np.array([-1, -1, 1])*(WIDTH//4) + center
    f = np.array([1, -1, 1])*(WIDTH//4) + center
    g = np.array([1, 1, 1])*(WIDTH//4) + center
    h = np.array([-1, 1, 1])*(WIDTH//4) + center
    return np.array([a, b, c, d, e, f, g, h])

def drawCube(screen, vertex):
    pg.draw.line(screen, "white", vertex[0][0:2], vertex[1][0:2])
    pg.draw.line(screen, "white", vertex[1][0:2], vertex[2][0:2])
    pg.draw.line(screen, "white", vertex[2][0:2], vertex[3][0:2])
    pg.draw.line(screen, "white", vertex[3][0:2], vertex[0][0:2])

    pg.draw.line(screen, "white", vertex[4][0:2], vertex[5][0:2])
    pg.draw.line(screen, "white", vertex[5][0:2], vertex[6][0:2])
    pg.draw.line(screen, "white", vertex[6][0:2], vertex[7][0:2])
    pg.draw.line(screen, "white", vertex[7][0:2], vertex[4][0:2])
    
    pg.draw.line(screen, "white", vertex[0][0:2], vertex[4][0:2])
    pg.draw.line(screen, "white", vertex[1][0:2], vertex[5][0:2])
    pg.draw.line(screen, "white", vertex[2][0:2], vertex[6][0:2])
    pg.draw.line(screen, "white", vertex[3][0:2], vertex[7][0:2])
    
    for i in range(len(vertex)): 
     pg.draw.circle(screen, "red", vertex[i][0:2], 3)
    
def project_points(points, projection_matrix):
    return np.array([projection_matrix @ points[i] for i in range(len(points))])

def rotateCube(screen, points, center, rot_matrix):
    points = points - center
    for i in range(len(points)):
        points[i] = rot_matrix @ points[i]  
    return points + center

def create3DrotationMatrix(theta):
    rot_matrix_z = np.array([
                            [np.cos(theta), -np.sin(theta), 0],
                            [np.sin(theta), np.cos(theta), 0],
                            [0, 0, 1]
                            ])

    rot_matrix_y = np.array([
                            [np.cos(theta), 0, np.sin(theta)],
                            [0, 1, 0],
                            [-np.sin(theta), 0, np.cos(theta)]
                            ])

    rot_matrix_x = np.array([
                            [1, 0, 0],
                            [0, np.cos(theta), -np.sin(theta)],
                            [0, np.sin(theta), np.cos(theta)]
                            ])

    return rot_matrix_x, rot_matrix_y, rot_matrix_z

def rotate3D(screen, points, center, rot_matrix, proj_matrix):
    rotated_points = rotateCube(screen, points, center, rot_matrix)
    projected_points = project_points(rotated_points, proj_matrix) + [WIDTH//6, -HEIGHT//8, 0]
    drawCube(screen, projected_points)
