import pyautogui as gui

class Algorithm:
	def __init__(self, templates, originCoords)
	self.imgs = templates
	self.boardX = originCoords[0]
	self.boardY = originCoords[1]

	def scanBoard(boardX, boardY):
		locs = []
		for t in templates:
			for l in gui.locateAllOnScreen(imgs[t]):
				locs.append(l, t)
		locs.sort()
		return locs

	def checkNormal():
		for i in range(8):
			pass

	def checkPatterns():
		for p in patterns:
			pass
			#check pattern
			#if pattern, mark