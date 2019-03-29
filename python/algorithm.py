import pyautogui as gui
from minePlane import MinePlane

class Algorithm:
	def __init__(self, bX, bY, mpargs):
		self.boardX = bX
		self.boardY = bY
		self.plane = MinePlane(mpargs[0], mpargs[1], mpargs[2])

	def flagNormal(self, board):
		for c in board:
			for r in c:
				if board[c][r] > 0 and board[c][r] < 9: #it's a number square
					mineCount = board[c][r]
					mineCount -= countFlags(board, c, r)
					if mineCount > 0: #not all mines are flagged
						unknownCount = countUnknowns(board, c, r)
						if unknownCount == mineCount:
							for i in range(-1, 2):
								for j in range(-1, 2):
									if c+i >= 0 and r+j >= 0 and board[c+i][r+j] == 9: #no backwards array iterating
										gui.click(self.plane.getCoords(board[c+i][r+j]), button="right")
					



	def flagPatterns(self):
		for p in self.patterns:
			pass
			#check pattern
			#if pattern, mark

	def countFlags(self, board, r, c):
		flagCount = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if c+i >= 0 and r+j >= 0 and board[c+i][r+j] == 10: #no backwards array iterating
					flagCount += 1
		return flagCount

	def countUnknowns():
		unknownCount = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if c+i >= 0 and r+j >= 0 and board[c+i][r+j] == 9: #no backwards array iterating
					unknown += 1
		return unknownCount