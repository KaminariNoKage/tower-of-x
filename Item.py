#Kai Austin & Michael Ninh
#Objinteract.py
#For class objects the user is intended to interact with

import pygame
from pygame.locals import *

red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

class Lock(pygame.sprite.Sprite):
    """ A 'lock' item, like a button or a lever that can open/close a door
    or cause a menu to pop up """
    def __init__(self, coord, size, doorlock, namefunc, color=green):
        #Parent constructor
        pygame.sprite.Sprite.__init__(self)

        x = coord[0]
        y = coord[1]
        
        #Making the Trigger
        self.image = pygame.Surface(size)
        self.image.fill(color)

        #Keeping tract of topleft corner
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
        #The specific door(s) the lock interacts with
        #Taken as a list?
        self.door = doorlock
        self.func = namefunc #Int, type of puzzle (0,1,2)
        
    def dunlock(self, doorindex):
        """ Unlocks a specific door given the index in a list """
        self.door[doorindex].open_door()
        #self.image = pygame.Surface([0,0])
        #self.rect = self.image.get_rect()

    def dlock(self, doorindex):
        """ Locks a specific door given the index in a list """
        self.door[doorindex].close_door()
        #self.image = pygame.Surface([0,0])
        #self.rect = self.image.get_rect()

    
