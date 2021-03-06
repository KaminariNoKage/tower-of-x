#Kai Austin & Michael Ninh
#popmenu.py
#Creates a Pop up menu in the game screen for puzzles

import pygame
import sys
sys.path.insert(0, 'project')
sys.path.insert(0, 'project/base_control')
import inputbox
import getPuzzle
from pygame.locals import *

def generate(lock):
    """ Generates a puzzle, a string for the question, and an answer """
    puzzle_type = lock.func #Get the type of puzzle the lock calls for
    new_puzzle = getPuzzle.Puzzle(puzzle_type)
    problem = new_puzzle.puzzle.display
    return new_puzzle, problem

def getinput(scrn, character, lock):
    puzzle, string = generate(lock) #Generate a puzzle
    answer = inputbox.ask(scrn, string) #Will get a string with answer
    cleared = puzzle.checkAnswer(character, answer)
    print cleared
    if cleared == True: #Determines if true or not
        return True #If true, win and door does what wants
    else:
        getinput(scrn, character, lock) #Else, repeat

