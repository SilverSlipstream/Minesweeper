import pyautogui as gui
import random
import algorithm as alg

imgs = ["imgs\\emptysquare.png", "imgs\\1mine.png", "imgs\\2mine.png", "imgs\\3mine.png",
	"imgs\\4mine.png", "imgs\\5mine.png", "imgs\\6mine.png", "imgs\\7mine.png",
	"imgs\\8mine.png", "imgs\\unknownsquare.png""imgs\\lose.png"] #if Minesweeper shows a bomb, you lose

boardX, boardY = gui.locateOnScreen("imgs\\gameboard.png") #left, top, width, height
gui.click(boardX, boardY) #focus moves to the minesweeper instead of console
#board is 30x16 (wxh)

originX, originY = gui.locateCenterOnScreen(emptysquare)

alg = Algorithm(
	imgs,
	[boardX, boardY]
	)

interval = 0
loc = []
lose = False
guessRandomly = False

def guess():


def chord():
	#chord every single number

# while not lose:
	loc = alg.scanBoard(originX, originY)
	for l in loc:
		print(loc[l])
# 	alg.checkNormal()
# 	guessRandomly = alg.checkPatterns()
# 	if (guessRandomly)
# 	{
# 		guess()
# 	}
# 	chord()

# if lose:
# 	print("Uh oh! I lost.")
# else:
# 	print("Yay! I won!")