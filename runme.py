# A script to visualise the potential in the 2D space around point sources of a field obeying the inverse square law
# (c) 2015 Christopher Stone

#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

import pygame
import time
import random
import math
import os
import string

#Set working directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#setup window
winsize = (1000, 1000)
winname = 'Monopole field plotter'
window = pygame.display.set_mode(winsize)
pygame.display.set_caption(winname)

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

class particle:
    def __init__(self, charge, x, y):
        self.x = x
        self.y = y
        self.charge = charge
        if self.charge == 0:
            self.colour = BLACK
        elif self.charge > 0:
            self.colour = RED
        elif self.charge < 0:
            self.colour = BLUE
    def draw(self):
        pygame.draw.circle(window, self.colour, (self.x, self.y), 5)

# Some example particles - note that charge can be negative
particles = []
particles.append(particle(200, 500, 0))
particles.append(particle(200, 500, 1000))

# special value that gives a cross in the centre of the image in this initial example
scalefact=1115630
    
interleave = True
initialrow = 0
initialcolumn = 0

if interleave:
    print "interleaving is on"
else:
    print "interleaving is off"
    
notclosed = True
while notclosed:  
    #Keeping track of the row and column currently being drawn
    row = initialrow
    column = initialcolumn
    while row < winsize[1]:
        column = initialcolumn
        while column < winsize[0]:
            total = 0
            for particle in particles:
                distance = 0.001+math.hypot(column-particle.x, row-particle.y)
                effect = (1/(distance**2))*particle.charge
                total += effect
            shade = (total*scalefact)%255
            pygame.draw.circle(window, (shade, shade, shade), (column, row), 0, 0)
            if interleave:
                column += 2
            else:
                column += 1
        pygame.display.flip()
        if interleave:
            row += 2
        else:
            row += 1
    for particle in particles:
        particle.draw()
    if interleave:
        if initialrow==0:
            initialrow+=1
        elif initialrow==1 and initialcolumn==0:
            initialrow=0
            initialcolumn=1
        elif initialrow==1 and initialcolumn==1:
            initialrow=0
            initialcolumn=0
        print initialrow
        print initialcolumn
    pygame.display.flip()
   # scalefact += 1 #can put things here to sequentially draw slightly different scenes
    print scalefact
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            notclosed = False
