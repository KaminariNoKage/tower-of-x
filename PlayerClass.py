#Kai Austin & Michael Ninh
#Software Design, Final Project
#character.py
#Contains the Class and methods for a Sprite/char
#Along with various related helper functions

import sys
sys.path.insert(0, './menu_key')
import pygame
import PopPuzzle
import CharacterClass
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, nowroom, newChar, img='ball.gif'):
        """
        Initializing the Character
        """
        pygame.sprite.Sprite.__init__(self)
        
        #Making the new Character
        self.character = CharacterClass.make_char(newChar)
        
        #Creating the image character
        self.image = pygame.Surface([20,20])
        self.image.fill((0, 0, 255))
        #self.image = pygame.image.load(img)

        #Speed vectors
        self.speedx = 0
        self.speedy = 0

        #Make top left corner the pass in
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

        #Keep track of the current room and other stat stuff
        self.current = nowroom.room.nameid

    def changespeed(self, x, y):
        self.speedx += x
        self.speedy += y

    def keydown(self, key):
        """ When a key is held down, move """
        if (key == K_RIGHT):
            self.changespeed(1,0)
        elif (key == K_LEFT):
            self.changespeed(-1,0)
        elif (key == K_UP):
            self.changespeed(0,-1)
        elif (key == K_DOWN):
            self.changespeed(0,1)
    
    def keyup(self, key):
        if (key == K_RIGHT):
            self.speedx = 0
            #self.moveR = False
        elif (key == K_LEFT):
            self.speedx = 0
            #self.moveL = False
        elif (key == K_UP):
            self.speedy = 0
            #self.moveU = False
        elif (key == K_DOWN):
            self.speedy = 0
            #self.moveD = False

    # Find a new position for the player
    def update(self, screen, curroom):
        # Get previous position
        oldx = self.rect.topleft[0]
        oldy = self.rect.topleft[1]
     
        # Update position
        newx = oldx + self.speedx
        newy = oldy + self.speedy
     
        # Put the player in the new spot
        self.rect.topleft = (newx,newy)

        #Check interaction between all items in the room
        self.manage_walls(curroom, oldx, oldy)
        self.manage_doors(curroom, oldx, oldy)
        self.manage_item(screen, curroom, oldx, oldy)
        self.check_teleport(curroom, oldx, oldy)

    def manage_walls(self, rm, ox, oy):
        """ Manages the case where player runs into wall """
        walls = rm.walls
        # Did this update cause us to hit a wall?
        collide_wall = pygame.sprite.spritecollide(self, walls, False)
        if collide_wall:
            #If collided, thrn go back to old position
            self.rect.topleft = (ox,oy)

    def manage_doors(self, rm, ox, oy):
        """ Manages the doors """
        doors = rm.doors
        # Did this update cause us to hit a door
        collide_door = pygame.sprite.spritecollide(self, doors, False)
        if collide_door:
            #If collided, thrn go back to old position
            self.rect.topleft = (ox,oy)

    def manage_item(self, scrn, rm, ox, oy):
        """ Manage the different items the player collides with """
        items = rm.room.allroom['allitems']
        # Did this update cause us to touch an item
        # Get the item in the index the player collided with
        itemindex = self.rect.collidelist(items)
        if itemindex >= 0:
            #If collided (more than -1), then go back to old position
            self.rect.topleft = (ox,oy)
            #Figure out which item collided with collided
            handle_item(self, scrn, rm, itemindex)
            #And set stuff to zero because stuff pops up
            self.speedx = 0
            self.speedy = 0

    def check_teleport(self, rm, ox, oy):
        """
        Checks whether or not the character hits a teleport
        If it does, then handles the return case of which screen 
        to transfer to
        """
        ports = rm.room.allroom['allports']
        # Touch portal? Which one?
        portindex = self.rect.collidelist(ports)
        if portindex >= 0:
            #Stop the player
            self.rect.topleft = (ox,oy)
            self.speedx = 0
            self.speedy = 0
            #Handle the teleport situation
            handle_teleport(self, rm, portindex)
        
        
            
       
def handle_item(player, screen, rm, lockkey):
    """
    Should there be a collision between a player and a lock, this
    will activate puzzle that will open/close a given door
    """

    all_locks = rm.room.allroom['allitems'] #Getting the locks in a room
    workinglock = all_locks[lockkey] #Getting the specific one collided with

    workingdoor = workinglock.door[0]
    temp = PopPuzzle.getinput(screen, player.character, workinglock)
    if temp:
        if workingdoor.closed:
            workinglock.dunlock(0)
        else:
            workinglock.dlock(0)

def handle_teleport(player, roomin, portroomid):
    """ 
    Handles the teleport situation. If a player collides with a teleport
    must determine which room to transfer, then change the case of the
    current room.
    """
    #Get the name of the room to teleport to
    tt = roomin.room.allroom['allports']
    teleport_to = tt[portroomid].portal
    
    #Changing the room the player should be in
    player.current = teleport_to
