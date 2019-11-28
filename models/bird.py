from OpenGL.GL import *
from OpenGL.GLU import *

from matrix_transformations.translation import *

class Bird():
    def __init__ (self, verticies, edges, surfaces, colors):
        self.verticies = verticies
        self.edges = edges
        self.surfaces = surfaces
        self.colors = colors

    def render_object(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.verticies[vertex])
        glEnd()

        glBegin(GL_QUADS)
        for surface in self.surfaces:

            for vertex in surface:
                glColor3fv(self.colors[0])
                glVertex3fv(self.verticies[vertex])
        

        # x = 0
        # for surface in surfaces:
        #     x += 1
        #     for vertex in surface:
        #         glColor3fv(colors[x])
        #         glVertex3fv(vertices[vertex])

        glEnd()
    
    def move_obstacle(self, tx, ty, tz):
        self.verticies = translate(self.verticies, tx, ty, tz)
        print(self.verticies[-1][-1])