import pyautogui as gui
import random
import algorithm as alg
#import cv2

unknownsquare = "unknownsquare.png"
emptysquare = "emptysquare.png"
1mine = "1mine.png"
2mine = "2mine.png"
3mine = "3mine.png"
4mine = "4mine.png"
5mine = "5mine.png"
6mine = "6mine.png"
7mine = "7mine.png"
8mine = "8mine.png"
gameOver = "lose.png" #if ms shows a bomb, you lose

boardDimensions = gui.locateOnScreen("imgs\\gameboard.png") #left, top, width, height
gui.click(boardDimensions[0], boardDimensions[1]) #focus moves to the minesweeper
#board is 30x16 (wxh)

originx, originy = gui.locateCenterOnScreen(emptysquare)
interval = 0
loc = [16][30]
lose = False
guessRandomly = False

def guess():


def chord():
	#chord every single number

while not lose:
	alg.scanBoard()
	alg.checkNormal()
	guessRandomly = alg.checkPatterns()
	if (guessRandomly)
	{
		guess()
	}
	chord()

if lose:
	print("Uh oh! I lost.")
else:
	print("Yay! I won!")