#Kai Austin & Michael Ninh
#Software Design Final Project Fall 2012
#Floor1_data.py

#The follow is the data used to make and create the different
#Rooms on the first floor. Note, it will not make all the rooms
#At once - it will make the room as needed (triggered by teleports)
#and then keep it in memory so it will not have to do so again.

import sys
sys.path.insert(0, 'project')
import RoomBuild as rb
import Item as item

green = 0, 255, 0

def make_111(scrn):
    nameid = (1,1,1)
    try:
        rooma = rb.RoomTopLeft(nameid, scrn)
        rooma.add_wall(rb.Wall([0, 300], [350, 50]))
        rooma.add_wall(rb.Wall([500, 300], [300, 50]))
        rooma.add_door(rb.Door(350, 300, 150, 10))

        doortemp = rooma.allroom['alldoors']
        newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
        rooma.add_item(newlock)

        return rooma
    except:
        print 'Error in Floor 1, Room 1'

def make_112(scrn):
    nameid = (1,1,2)
    roomb = rb.RoomLeft(nameid, scrn)
    roomb.add_wall(rb.Wall([0, 300], [350, 50]))
    roomb.add_wall(rb.Wall([500, 300], [300, 50]))
    roomb.add_door(rb.Door(350, 300, 150, 10))

    doortemp = roomb.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    roomb.add_item(newlock)

    return roomb

def make_113(scrn):
    nameid = (1,1,3)
    nroom = rb.RoomBottomLeft(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_121(scrn):
    nameid = (1,2,1)
    nroom = rb.RoomTop(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_122(scrn):
    nameid = (1,2,2)
    nroom = rb.RoomCenter(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_123(scrn):
    nameid = (1,2,3)
    nroom = rb.RoomBottom(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_131(scrn):
    nameid = (1,3,1)
    nroom = rb.RoomTopRight(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_132(scrn):
    nameid = (1,3,2)
    nroom = rb.RoomRight(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_133(scrn):
    nameid = (1,3,3)
    nroom = rb.RoomBottomRight(nameid, scrn)
    nroom.add_wall(rb.Wall([0, 300], [350, 50]))
    nroom.add_wall(rb.Wall([500, 300], [300, 50]))
    nroom.add_door(rb.Door(350, 300, 150, 10))

    doortemp = nroom.allroom['alldoors']
    newlock = item.Lock([600, 10], [10, 10], doortemp, 0)
    nroom.add_item(newlock)

    return nroom

def make_Floor1(screen):
    r111 = make_111(screen)
    r112 = make_112(screen)
    r113 = make_113(screen)
    r121 = make_121(screen)
    r122 = make_122(screen)
    r123 = make_123(screen)
    r131 = make_131(screen)
    r132 = make_132(screen)
    r133 = make_133(screen)

    floor = rb.Floor()
    floor.add_room(r111.nameid, r111)
    floor.add_room(r112.nameid, r112)
    floor.add_room(r113.nameid, r113)
    floor.add_room(r121.nameid, r121)
    floor.add_room(r122.nameid, r122)
    floor.add_room(r123.nameid, r123)
    floor.add_room(r131.nameid, r131)
    floor.add_room(r132.nameid, r132)
    floor.add_room(r133.nameid, r133)

    return floor
