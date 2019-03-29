import pyautogui as gui

class MinePlane:
	def __init__(self, templates, dimens, intrvl):
		self.imgs = templates
		self.dimensions = dimens
		self.origin = (self.dimensions[0] + 16, self.dimensions[1] + 16)
		self.interval = intrvl
		self.plane = []
		for i in range(30):
			self.plane.append([])
			for j in range(16):
				self.plane[i].append(-1)

	def scanBoard(self):
		for i in range(len(self.imgs)):
				for pos in gui.locateAllOnScreen(self.imgs[i], region=self.dimensions, confidence=0.9):
					x, y = self.getCoords(pos[0], pos[1])
					self.plane[x][y] = i
		return self.plane

	def getCoords(self, x, y): #coordinate plane values
		retX = x - self.origin[0]
		retX /= self.interval
		retY = y - self.origin[1]
		retY /= self.interval
		return int(retX), int(retY)

	def getLocs(self, x, y): #actual location on screen
		retX = self.origin[0]
		retX += x * self.interval
		retY = self.origin[1]
		retY += y * self.interval
		return retX, retY

	def getType(self, x, y):
		self.squareType = self.plane[x][y]
		return squareType