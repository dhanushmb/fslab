import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height),DOUBLEBUF|OPENGL)
pygame.display.set_caption("3D Transformations")
glClearColor(0.0, 0.0, 0.0, 1.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (screen_width / screen_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
vertices = np.array([[-1, -1, -1],[1, -1, -1],[1, 1, -1],[-1, 1, -1],[-1, -1, 1],[1, -1, 1],[1, 1, 1],[-1, 1, 1]], dtype=np.float32)
edges = np.array([[0, 1], [1, 2], [2, 3], [3, 0],[4, 5], [5, 6], [6, 7], [7, 4],[0, 4], [1, 5], [2, 6], [3, 7]], dtype=np.uint32)
translation_matrix = np.eye(4, dtype=np.float32)
translation_matrix[3, :3] = [0, 0, -5]
rotation_matrix = np.eye(4, dtype=np.float32)
scaling_matrix = np.eye(4, dtype=np.float32)
scaling_matrix[0, 0] = 1.5
scaling_matrix[1, 1] = 1.5
scaling_matrix[2, 2] = 1.5
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glMultMatrixf(translation_matrix)
    glRotatef(angle, 1, 1, 0)
    glMultMatrixf(rotation_matrix)
    glMultMatrixf(scaling_matrix)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3iv(vertices[vertex])
    glEnd()
    angle += 1
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
