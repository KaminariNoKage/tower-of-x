#Kai Austin & Michael Ninh
#Room_build.py
#Holds all the classes and helper functions relating to Walls and Solid objects

import pygame
import Item as item
from pygame.locals import *

white = 255, 255, 255
black = 0,0,0
green = 0, 255, 0

class Wall(pygame.sprite.Sprite):
    """    Making Wall   """
    def __init__(self, location=[0,0], size=[0,0], color=white):
        #Call the parent constructor
        pygame.sprite.Sprite.__init__(self)

        #Unpack
        x = location[0]
        y = location[1]
        #size = [width, height]
        
        #Make a wall
        self.image = pygame.Surface(size)
        self.image.fill(color)

        #Make top-left corner passed-in location
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
#These make default Border walls
defx = 0
defy = 0
defwid = 10
defhei = 10

def make_topwall(scrn_width):
    """ Wall for the entire top of displayed screen """
    loc = [defx, defy]
    size = [scrn_width, defhei]
    new_wall = Wall(loc, size)
    return new_wall

def make_leftwall(scrn_height):
    """ Wall for the entire left of displayed screen """
    loc = [defx, defy]
    size = [defwid, scrn_height]
    new_wall = Wall(loc, size)
    return new_wall

def make_bottomwall(scrn_width, scrn_height):
    """ Wall for the entire bottom of displayed screen """
    loc = [defx, (scrn_height - defhei)]
    size = [scrn_width, defhei]
    new_wall = Wall(loc, size)
    return new_wall

def make_rightwall(scrn_width, scrn_height):
    """ Wall for the entire right of displayed screen """
    loc = [(scrn_width - defwid), defy]
    size = [defwid, scrn_height]
    new_wall = Wall(loc, size)
    return new_wall

class Door(pygame.sprite.Sprite):
    """ Makes a door """
    def __init__(self, x, y, width, height, color=white, closed=True):
        #Call the parent constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        #Make top-left corner passed-in location
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        #Make initial for purpose of rebuilding when shut
        self.initx = x
        self.inity = y
        self.initwidth = width
        self.initheight = height
        self.initcolor = color
        
        if closed:
            self.closed = True

    def open_door(self):
        #opens the door by changing its size
        self.image = pygame.Surface([0,0])
        self.rect = self.image.get_rect()
        self.closed = False

    def close_door(self):
        """ Return Door to initial configurations """
        x = self.initx
        y = self.inity
        w = self.initwidth
        h = self.initheight
        color = self.initcolor

        self.image = pygame.Surface([w,h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.closed = True

class Teleport(pygame.sprite.Sprite):
    """
    A teleport transfers the player from one room to another
    The teleport itself is a specific area. When the player comes in contact
    they will be moved to another room.
    """
    def __init__(self, location, size, wormhole):
        #Parent constructor
        pygame.sprite.Sprite.__init__(self)

        #Redefining
        x = location[0]
        y = location[1]
        #Note: size = [width, height]
        
        #Making the sprite object
        self.image = pygame.Surface(size)
        self.image.fill(black)

        #Record of top-left corner
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        #Room which the teleport connects
        #Note, this is a tuple (floor,x,y)
        self.portal = wormhole

#Default full border teleports
tdefx = 0
tdefy = 0
tdefwid = 1
tdefhei = 1

def make_topport(scrn_width, port):
    """ Teleport for the entire top of displayed screen """
    loc = [tdefx, tdefy]
    size = [scrn_width, tdefhei]
    new_port = Teleport(loc, size, port)
    return new_port

def make_leftport(scrn_height, port):
    """ Teleport for the entire left of displayed screen """
    loc = [tdefx, tdefy]
    size = [tdefwid, scrn_height]
    new_port = Teleport(loc, size, port)
    return new_port

def make_bottomport(scrn_width, scrn_height, port):
    """ Wall for the entire bottom of displayed screen """
    loc = [tdefx, (scrn_height-1)]
    size = [scrn_width, tdefhei]
    new_port = Teleport(loc, size, port)
    return new_port

def make_rightport(scrn_width, scrn_height, port):
    """ Wall for the entire right of displayed screen """
    loc = [(scrn_width-1), tdefy]
    size = [tdefwid, scrn_height]
    new_port = Teleport(loc, size, port)
    return new_port

class Room(object):
    """ 
    Makes a Room 
    A room can consist of the following:
    - Walls
    - Doors
    - "Teleports" to other rooms
    - Locks + Puzzles
    - Items (if avalible)
    """
    def __init__(self, name):
        """ Creating the Room, along with base walls, doors, and objects """
        #More specifically refers to coordinates
        #Floor (1 2 3), X(1 2 3), Y (1 2 3) = (F,X,Y)
        self.nameid = name
        
        #where Everything in the room is stored (in lists)
        self.allroom = dict()

        #Making dictionary references
        self.allroom['allwalls'] = []
        self.allroom['alldoors'] = []
        self.allroom['allports'] = []
        self.allroom['allitems'] = []

    def add_wall(self, wall):
        """        
        Adds a wall to the room        
        """
        self.allroom['allwalls'].append(wall)

    def add_door(self, door):
        """        
        Adds a door to the room        
        """
        self.allroom['alldoors'].append(door)
    
    def add_port(self, teleport):
        """        
        Adds a teleport to the room        
        """
        self.allroom['allports'].append(teleport)
    
    def add_item(self, item):
        """       
        Adds an item (based on name/type) to the room        
        """
        self.allroom['allitems'].append(item)

class RoomTopLeft(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)

        #Making the Default Walls
        width, height = scrnsize
        topwall = make_topwall(width)
        self.add_wall(topwall)
        leftwall = make_leftwall(height)
        self.add_wall(leftwall)

        #Making the default teleports
        floor, xplace, yplace = name
        rport = (floor, xplace+1, yplace)
        bport = (floor, xplace, yplace+ 1)

        rightport = make_rightport(width, height, rport)
        self.add_port(rightport)
        bottomport = make_bottomport(width, height, bport)
        self.add_port(bottomport)

class RoomTop(Room):
    """
    Makes a default for corner room on the top
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)

        #Making the Default Walls
        width, height = scrnsize
        topwall = make_topwall(width)
        self.add_wall(topwall)

        #Making the default teleports
        floor, xplace, yplace = name
        lport = (floor, xplace-1, yplace)
        rport = (floor, xplace+1, yplace)
        bport = (floor, xplace, yplace+ 1)

        leftport = make_leftport(height, lport)
        self.add_port(leftport)
        rightport = make_rightport(width, height, rport)
        self.add_port(rightport)
        bottomport = make_bottomport(width, height, bport)
        self.add_port(bottomport)

class RoomTopRight(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        #Making the Default Walls
        width, height = scrnsize

        topwall = make_topwall(width)
        self.add_wall(topwall)
        rightwall = make_rightwall(width, height)
        self.add_wall(rightwall)

        #Making the default teleports
        floor, xplace, yplace = name
        lport = (floor, xplace-1, yplace)
        bport = (floor, xplace, yplace+ 1)

        leftport = make_leftport(height, lport)
        self.add_port(leftport)
        bottomport = make_bottomport(width, height, bport)
        self.add_port(bottomport)

class RoomLeft(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        #Making the Default Walls
        width, height = scrnsize

        leftwall = make_leftwall(height)
        self.add_wall(leftwall)

        #Making the default teleports
        floor, xplace, yplace = name
        tport = (floor, xplace, yplace- 1)
        rport = (floor, xplace+1, yplace)
        bport = (floor, xplace, yplace+ 1)

        topport = make_topport(width, tport)
        self.add_port(topport)
        rightport = make_rightport(width, height, rport)
        self.add_port(rightport)
        bottomport = make_bottomport(width, height, bport)
        self.add_port(bottomport)

class RoomCenter(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        width, height = scrnsize

        #Making the default teleports
        floor, xplace, yplace = name
        tport = (floor, xplace, yplace- 1)
        lport = (floor, xplace-1, yplace)
        rport = (floor, xplace+1, yplace)
        bport = (floor, xplace, yplace+ 1)

        topport = make_topport(width, tport)
        self.add_port(topport)
        leftport = make_leftport(height, lport)
        self.add_port(leftport)
        rightport = make_rightport(width, height, rport)
        self.add_port(rightport)
        bottomport = make_bottomport(width, height, bport)
        self.add_port(bottomport)

class RoomRight(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        #Making the Default Walls
        width, height = scrnsize

        rightwall = make_rightwall(width, height)
        self.add_wall(rightwall)

        #Making the default teleports
        floor, xplace, yplace = name
        tport = (floor, xplace, yplace- 1)
        lport = (floor, xplace-1, yplace)
        bport = (floor, xplace, yplace+ 1)

        topport = make_topport(width, tport)
        self.add_port(topport)
        leftport = make_leftport(height, lport)
        self.add_port(leftport)
        bottomport = make_bottomport(width, height, bport)
        self.add_port(bottomport)

class RoomBottomLeft(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        #Making the Default Walls
        width, height = scrnsize

        bottomwall = make_bottomwall(width, height)
        self.add_wall(bottomwall)
        leftwall = make_leftwall(height)
        self.add_wall(leftwall)

        #Making the default teleports
        floor, xplace, yplace = name
        tport = (floor, xplace, yplace- 1)
        rport = (floor, xplace-1, yplace)

        topport = make_topport(width, tport)
        self.add_port(topport)
        rightport = make_rightport(width, height, rport)
        self.add_port(rightport)

class RoomBottom(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        #Making the Default Walls
        width, height = scrnsize
        bottomwall = make_bottomwall(width, height)
        self.add_wall(bottomwall)

        #Making the default teleports
        floor, xplace, yplace = name
        tport = (floor, xplace, yplace- 1)
        lport = (floor, xplace-1, yplace)
        rport = (floor, xplace+1, yplace)

        topport = make_topport(width, tport)
        self.add_port(topport)
        leftport = make_leftport(height, lport)
        self.add_port(leftport)
        rightport = make_rightport(width, height, rport)
        self.add_port(rightport)

class RoomBottomRight(Room):
    """
    Makes default for corner room on the top right
    """
    def __init__(self, name, scrnsize):
        #Parent Constructor
        Room.__init__(self, name)
        
        #Making the Default Walls
        width, height = scrnsize
        bottomwall = make_bottomwall(width, height)
        self.add_wall(bottomwall)
        rightwall = make_rightwall(width, height)
        self.add_wall(rightwall)

        #Making the default teleports
        floor, xplace, yplace = name
        tport = (floor, xplace, yplace- 1)
        lport = (floor, xplace-1, yplace)

        topport = make_topport(width, tport)
        self.add_port(topport)
        leftport = make_leftport(height, lport)
        self.add_port(leftport)

class Floor(object):
    """ 
    A 3X3 Floor "Grid" comprised of rooms. Stored as a dictionary
    """
    def __init__(self):
        #Place to put the rooms
        #|_0_|_1_|_2_|
        #|_3_|_4_|_5_|
        #|_6_|_7_|_8_|
        #Dictionary should read {(1,1,1):ROOM1, (1,1,2):ROOM2, ...etc}

        self.roomgrid = dict()
    
    def add_room(self, namekey, new_room):
        """ 
        Adding a new room to the floor
        """
        self.roomgrid[namekey] = new_room

    def get_room(self, name):
        """
        Getting a room on the floor
        """
        reqroom = self.roomgrid[name]
        return reqroom

class Tower(object):
    """ Comprised of Floors stacked on top of one another """
    def __init__(self):
        self.allFloors = []

    def add_floor(self, new_floor):
        """ Adds a new floor on top of the tower """
        self.allFloors.append(new_floor)
