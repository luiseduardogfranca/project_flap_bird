import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from models.obstacle import Obstacle
from models.bird import Bird

from models.obstacle_coordinates import *
from models.bird_coordnates import *

from enviroment.env_variables import *

import random

rotated = False
lock = 500

obstacles = [
    Obstacle(verticies, edges, surfaces, colors),
    Obstacle(verticies, edges, surfaces, colors),
    Obstacle(verticies, edges, surfaces, colors),
    Obstacle(verticies, edges, surfaces, colors),
    ]

for i in obstacles:
    i.move_obstacle(random.uniform(-2,2), random.uniform(-2,2), random.uniform(0,-4))

bird = Bird(bird_verticies, bird_edges, bird_surfaces, bird_colors)
bird.move_obstacle(0,0,2)



def main():
    global rotated
    global lock
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) # Default shit

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    #glRotatef(-90,0,1,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.move_obstacle(0,0.25,0)
                if event.key == pygame.K_LEFT:
                    bird.move_obstacle(-0.1,0,0)
                if event.key == pygame.K_RIGHT:
                    bird.move_obstacle(0.1,0,0)
        
        for i in obstacles:
            if i.verticies[-1][-1] <= 3:
                i.move_obstacle(0,0,.02)
            else:
                i.move_obstacle(random.uniform(-2,2), random.uniform(-2,2), random.uniform(-6,-8))
        

        bird.move_obstacle(0,-0.01,0)

        if rotated == False and lock <= 0:
            aux = random.randint(0,5)
            if aux <= 2.5:
                glRotatef(-90,0,1,0)
                lock = 500
                rotated = True
        if rotated == True and  lock <= 0:
            aux = random.randint(0,5)
            if aux <= 2.5:
                glRotatef(90,0,1,0)
                lock = 500
                rotated = False
        
        lock -= 1

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)



        bird.render_object()

        for i in obstacles:
            i.render_object()
        pygame.display.flip() #Test pygame.display.update()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()