#!/usr/bin/python

import pygame
import random 
import time

FPS = 60
CELLSIZE = 15 
SCREENWIDTH = CELLSIZE * 36 
SCREENHEIGHT = CELLSIZE * 36

def main():
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    GAMERUNNING = True
    colors = [ (0x07,0x07,0x07), (0x1F,0x07,0x07), (0x2F,0x0F,0x07), (0x47,0x0F,0x07), (0x57,0x17,0x07), (0x67,0x1F,0x07), (0x77,0x1F,0x07), (0x8F,0x27,0x07), (0x9F,0x2F,0x07), (0xAF,0x3F,0x07), (0xBF,0x47,0x07), (0xC7,0x47,0x07), (0xDF,0x4F,0x07), (0xDF,0x57,0x07), (0xDF,0x57,0x07), (0xD7,0x5F,0x07), (0xD7,0x5F,0x07), (0xD7,0x67,0x0F), (0xCF,0x6F,0x0F), (0xCF,0x77,0x0F), (0xCF,0x7F,0x0F), (0xCF,0x87,0x17), (0xC7,0x87,0x17), (0xC7,0x8F,0x17), (0xC7,0x97,0x1F), (0xBF,0x9F,0x1F), (0xBF,0x9F,0x1F), (0xBF,0xA7,0x27), (0xBF,0xA7,0x27), (0xBF,0xAF,0x2F), (0xB7,0xAF,0x2F), (0xB7,0xB7,0x2F), (0xB7,0xB7,0x37), (0xCF,0xCF,0x6F), (0xDF,0xDF,0x9F), (0xEF,0xEF,0xC7), (0xFF,0xFF,0xFF)];
    across = int(SCREENWIDTH / CELLSIZE)
    down = int(SCREENHEIGHT/ CELLSIZE)
    
    orig_cells = [] 
    startcol = 0 
    colorcounter = 0 
    for x in range(0, across * down):
            orig_cells.append(startcol)
            colorcounter += 1
            if colorcounter >= across:
                colorcounter =0 
                startcol += 1
    cells = orig_cells.copy()
    counter = 0 
    for x in range(0, across):
        for y in range(0, down):
            pygame.draw.rect(DISPLAYSURF, colors[cells[counter]], (y * CELLSIZE, x * CELLSIZE, CELLSIZE, CELLSIZE))
            counter += 1

    while GAMERUNNING == True: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                GAMERUNNING = False
        counter = 0 
        for x in range(0, across - 1):
            for y in range(0, down):
                pygame.draw.rect(DISPLAYSURF, colors[cells[counter]], (y * CELLSIZE, x * CELLSIZE, CELLSIZE, CELLSIZE))
                counter += 1
                if counter >= across * (down - 1):
                    counter = 0 
                if random.randint(0,1) == 0:
                    cells[counter] = cells[counter + across]
                else:
                    cells[counter] = orig_cells[counter]
        pygame.display.flip()
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()

