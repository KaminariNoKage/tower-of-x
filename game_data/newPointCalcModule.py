'''fileName: newPointCalcModule
takes character in parameter, should be able to tally up total points'''

import time 
import getPuzzle

class pointsCalc(object):
    def __init__(self,puzzleType):
        self.__startTime = time.time()
        self.__puzzleType = puzzleType
    def startPoints(self,puzzleType):
        if self.__puzzleType == 0:
            self.__MStartingPoints = 100
        elif self.__puzzleType == 1:
            self.__AStartingPoints = 200
        elif self.__puzzleType == 2:
            self.__LStartingPoints = 1000
    def puzzleDuration(self):
        self.__duration = time.time()-self.__startTime
        #print 'You took', '{0:.3g}'.format(self.__duration), 'seconds to answer'
    def puzzlePoints(self,character): #point branching
        if self.__puzzleType == 0:
            self.calculation = self.__MStartingPoints - (self.__duration*10)
            if self.calculation < 0:
                self.calculation = 0
                #print 'You took too long to answer.'
            #print 'you scored','{0:.3g}'.format(self.calculation), 'points!'
            character.addPoints(self.calculation) 
            return self.calculation
        elif self.__puzzleType == 1:
            self.calculation = self.__AStartingPoints - (self.__duration*10)
            if self.calculation < 0:
                self.calculation = 0
                #print 'You took too long to answer.'
            #print 'you scored','{0:.3g}'.format(self.calculation), 'points!'
            character.addPoints(self.calculation) 
            return self.calculation
        elif self.__puzzleType == 2:
            self.calculation = self.__LStartingPoints - (self.__duration*10)
            if self.calculation < 0:
                self.calculation = 0
                #print 'You took too long to answer.'
            #print 'you scored','{0:.3g}'.format(self.calculation), 'points!'
            character.addPoints(self.calculation) 
            return self.calculation
    
    def wrongAnswer(self,character):
        self.deduct = self.__duration*15
        character.losePoints(self.deduct)
        
    
        
        
