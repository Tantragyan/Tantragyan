# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:25:58 2020

@author: vyomk
"""

import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Mousemotion')
clock = pygame.time.Clock()
crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)
   
    
pygame.quit()
quit()