'''
Kai Austin & Micahel Ninh
Software Design Fall 2012
filename: getPuzzle
method for randomly selecting puzzles'''

import random
import sys 
sys.path.insert (0, './game_data')
import mathPuzzle
import anagramPuzzle
import logicPuzzle

class Puzzle(object):
    def __init__(self, ptype):
	#ptype in range 0 - 2
        self.type = ptype
        if ptype == 0:
             self.puzzle = mathPuzzle.mathPuzzle()
             #mathPuzzler.checkA(character)
        elif ptype == 1:
            self.puzzle = anagramPuzzle.anagramPuzzle()
            #anagramPuzzler.getWords()
            #anagramPuzzler.getAnswer()
            #anagramPuzzler.askQuestion(character)
        elif ptype == 2:
            self.puzzle = logicPuzzle.logicPuzzle()
            #logicPuzzler.getQuestion()
            #logicPuzzler.checkA(character)
            
    def checkAnswer(self, character, input_ans):
        """ Checks the answer to the above puzzle questions    """

        tval = False #By default incorrect

        if input_ans == '':
            #If the input is an empty string
            pass
        elif self.type == 0: #Else check everything else
            tval = self.puzzle.checkMath(character, input_ans)
        elif self.type == 1:
            tval = self.puzzle.checkAnagram(character, input_ans)
        elif self.type == 2:
            tval = self.puzzle.checkLogic(character, input_ans)

        #TRUE if answer correct, FALSE otherwise
        return tval
