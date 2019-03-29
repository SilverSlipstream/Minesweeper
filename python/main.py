import pyautogui as gui
import random
from algorithm import Algorithm
from minePlane import MinePlane

imgs = ["imgs\\emptysquare.png", "imgs\\1mine.png", "imgs\\2mine.png", "imgs\\3mine.png",
	"imgs\\4mine.png", "imgs\\5mine.png", "imgs\\6mine.png", "imgs\\7mine.png",
	"imgs\\8mine.png", "imgs\\unknownsquare.png", "imgs\\flag.png", "imgs\\lose.png"] #if Minesweeper shows a bomb, you lose

boardDimensions = gui.locateOnScreen("imgs\\gameboard.png") #left, top, width, height
gui.click(boardDimensions.left, boardDimensions.top) #focus moves to the minesweeper instead of console
#board is 30x16 (wxh)

interval = 23

minePlaneArgs = [imgs, boardDimensions, interval]
alg = Algorithm(boardDimensions[0], boardDimensions[1], minePlaneArgs)
plane = MinePlane(minePlaneArgs[0], minePlaneArgs[1], minePlaneArgs[2])



coords = []
lose = False
guessRandomly = False

def guess():
	while True:
		x = random.randrange(0,30, 1)
		y = random.randrange(0,16, 1)
		if coords[x][y] == 9:
			print(coords[x][y])
			print(plane.getLocs(x, y))
			gui.click(plane.getLocs(x, y))
			break
# def chordAll():
	#chord every single number
coords = plane.scanBoard()
guess()
while not lose:
	coords = plane.scanBoard()
	for i in range(len(coords)):
		print(coords[i])
	alg.flagNormal(coords)
	break
#	guessRandomly = alg.flagPatterns()
# 	if (guessRandomly)
# 	{
# 		guess()
# 	}
# 	chordAll()
	if gui.locateOnScreen(imgs[11]) != None:
		lose = False

# if lose:
# 	print("Uh oh! I lost.")
# else:
# 	print("Yay! I won!")