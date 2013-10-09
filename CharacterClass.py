'''fileName: character
keep track of emotion points, and total game points'''

import newPointCalcModule


class Character(object):
    def __init__(self, energy=0, frustration=0, totalPoints=0):
	self.charname = None
        self.energy = energy
        self.frustration = frustration
        self.totalPoints = totalPoints
    def posChange(self):
        self.energy += 1 
        self.frustration += 1 
    def negChange(self):
        self.energy -= 1 
        self.frustration -= 1 
    def addPoints(self,increase):
        self.totalPoints += increase
        print 'You have ' + str('{0:.3g}'.format(self.totalPoints)) + ' points'
    def losePoints(self,deduct):
        self.totalPoints -= deduct
        print 'You have ' + str('{0:.3g}'.format(self.totalPoints)) + ' points'
    def frustrationEnd(self):
        if self.frustration == 0:
            print 'Your character is too frustrated to continue. The journey has ended. YOU LOSE', 'You end the game with ' + str('{0:.3g}'.format(self.totalPoints)) + ' points.'
           

class Princess(Character):
    def __init__(self,energy=8,frustration=10,totalPoints=0):
        Character.__init__(self)
	self.charname = 'Princess'
        self.energy = energy
        self.frustration = 10
        self.totalPoints = 0
    
class Assassin(Character):
    def __init__(self,energy=12,frustration=10,totalPoints=0):
        Character.__init(self)
	self.charname = 'Assassin'
        self.energy = energy
        self.frustration = 10
        self.totalPoints = 10 
        self.totalPoints = 0

class Peasant(Character):
    def __init__(self,energy=9,frustration=9,totalPoints=0):
        Character.__init__(self)
	self.charname = 'Peasant'
        self.energy = energy
        self.frustration = frustration
        self.totalPoints = totalPoints

def make_char(charIndex):
    """
    Returns a new character given a specific index
    """
    if charIndex == 0:
        princess = Princess()
        return princess
    elif charIndex == 1:
        assassin = Assassin()
        return assassin
    elif charIndex == 2:
        peasant = Peasant()
        return peasant
