#Kai Austin & Michael Ninh
#Software Design Final Project Fall 2012
#Game: Tower of X
#runproj.py

import sys, os
sys.path.insert(0, './menu_key')
import pygame
from pygame.locals import *
import Item
import MainGameClass as cgame

#Variables for stuff
size = width, height = 700, 700
black = 0,0,0
white = 255,255,255

#Initializing Pygame
pygame.init()
  
#making screen
screen = pygame.display.set_mode(size)

#Need some function to display menu screen of choices
#New

world = cgame.World(size)
    
def main():
    """ The main function loop of the game """

    g = cgame.Game(size, world) #The new player's game itself
    d = g.curroom #The current screen/room
    pimg = g.player.image #The player's image
    prect = g.player.rect #The player's location
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == KEYDOWN:
                g.player.keydown(event.key)
            elif event.type == KEYUP:
                g.player.keyup(event.key)

        #Character update
        g.player.update(screen, d)
    
        #Visual update
        screen.fill(black)
        d.walls.draw(screen)
        d.doors.draw(screen)
        d.locks.draw(screen)
        screen.blit(pimg, prect)

        #Checking changes of rooms, etc.
        checkport = g.player.current
        if checkport != d.room.nameid:
            print checkport, d.room.nameid
            g.change_room(size, world, checkport)
            d = g.curroom

        pygame.display.flip()

##Activate the Game Here##
main()
