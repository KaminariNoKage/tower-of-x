#Kai Austin & Michael Ninh
#Software Design Fall 2012
#PortMath.py

#This file primarily calculates position of the character
#In the event of a collision with a teleport


def adjust_rect(scrn_size, currect, oldid, newid):
    """ 
    RETURNS [newxrect,newyrect]
    Find the new position the player has to be in based on the room
    change and which teleport has been hit (which pretty much is based
    on the type of room change)

    scrn_size = size of the screen [width, height]
    currect = the current top left corner of the player
    oldid = room moving from (f,x,y)
    newid = room moving to (f,x,y)

    Note: Walls have an offset of 10, as does the chararacter?
    """

    wd, ht = scrn_size     #Getting the relevant screen size here
    xrect, yrect = currect #Getting the character position
    oldfloor, oldxpos, oldypos = oldid    #Getting the old room id stuff
    newfloor, newxpos, newypos = newid    #Getting the new room id stuff

    #Set defaults to original position before teleport
    newxrect = xrect
    newyrect = yrect

    #Getting the differences between the rooms
    #Floors may vary, however rooms should only have a difference of +-1
    floorDiff = newfloor - oldfloor
    xDiff = newxpos - oldxpos
    yDiff = newypos - oldypos

    if floorDiff != 0:
        #If there is a change in floor, the rect should not change
        #(This might need to be adjusted later depending on design)
        #Right now this is a "straight up" teleport, not exactly stairs
        return [newxrect,newyrect]
    elif floorDiff == 0:
        #else if there is no change in the floor
        #This primarily addresses side teleports
        if xDiff == -1:
            #If going left <= right
            print 'left to right'
            newxrect = wd - 40 #Bring to right side of screen
        elif xDiff == 1:
            #If going left => right
            print 'right to left'
            newxrect = 10 #Bring to left side of screen
        
        if yDiff == -1:
            #If going from up <= down
            print 'down to up'
            newyrect = ht - 40 #Bring to bottom of screen
        elif yDiff == 1:
            #If going from up => down
            print 'up to down'
            newyrect = 10 #bring to top of screen

    return [newxrect, newyrect]
        
    

    
