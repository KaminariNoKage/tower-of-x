'''fileName: logicPuzzle
class for the logic puzzles
current problems: must put answer in quotations!!!
'''

import newPointCalcModule
import logicPuzzleQuestions
import random

class logicPuzzle(object):
    def __init__(self):
        self.__status = None
        self._timer = newPointCalcModule.pointsCalc(2)
        self._timer.startPoints(2)
        self.__book = logicPuzzleQuestions.logicPuzzleQuestions() #entire
        questions = self.__book.dictor() #questions able to extract
        self.__question = random.choice(questions.keys()) #question
        self.__answer = questions[self.__question]
        self.display = 'A door is either true or false. Which door should I take based on their hints?\n' + self.__question
        self._timer.puzzleDuration()

    def checkLogic(self,character, input_ans):
	print input_ans, self.__answer
        if input_ans == self.__answer:
            self.__status = True
            self._timer.puzzlePoints(character)#POINT/TIMER MODULE
            character.posChange()
            return self.__status
        else:
            self.__status = False
            self._timer.wrongAnswer(character) #POINT/TIMER MODULE
            character.negChange()
            character.frustrationEnd()
            return self.__status

        

        
        
    
        
