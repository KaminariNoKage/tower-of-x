#Kai Austin & Micahel Ninh
#MainGameClass.py

#These are all the main Classes that are used in the game
#along with the methods and functions to help them run

import sys
sys.path.insert(0, './game_data')
import pygame
from pygame.locals import *
import PlayerClass
import PortMath
import floor1_data as data


class Game(object):
    def __init__(self, screen, world):
        self.username = [] #REPALCE THIS (pass in username entered by user)
        #Making the starting room
        start = (1,1,1)
        self.curroom = CurrentRoom(screen, world, (1,1,2))
        #Put the player in starting position
        self.player = PlayerClass.Player(10,10, self.curroom, 0)
        self.world = World(screen) #keeps record of the game world
        #which can be accessed to later in the event user pauses
        self.score = [] #REPLACE THIS (keeps track of scoring system, etc)

    def change_room(self, screen, world, newid):
        """ Changes and re-renders the room the player is in """

        #Getting the old roomid
        oldroomid = self.curroom.room.nameid

        #Changes the player's position reflective of the room change
        #Based on player rect and old=>new room
        playpos = self.player.rect.topleft
        newrect = PortMath.adjust_rect(screen, playpos, oldroomid, newid)
        self.player.rect.topleft = newrect
	
        #Changes the current room
        self.curroom = CurrentRoom(screen, self.world, newid)
        
        

class CurrentRoom(object):
    """ Creating a new room """
    def __init__(self, scrn, world, roomid):
        #Making the room
        self.room = world.tower.get_room(roomid)
        wall_list = self.room.allroom['allwalls']
        door_list = self.room.allroom['alldoors']
        item_list = self.room.allroom['allitems']
        port_list = self.room.allroom['allports']
        self.walls = pygame.sprite.RenderPlain(wall_list)
        self.doors = pygame.sprite.RenderPlain(door_list)
        self.locks = pygame.sprite.RenderPlain(item_list)
        self.ports = pygame.sprite.RenderPlain(port_list)


class World(object):
    """ Creating the Game World """
    def __init__(self,scrn):
        self.mainMenu = [] #REPLACE WITH MAIN MENU SCREEN
        self.statView = [] #REPLACE WITH STAT VIEW MENU
        self.tower = data.make_Floor1(scrn) #For now, just one floor
