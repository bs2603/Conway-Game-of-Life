#This Code implements the rules of Conway's game of life using Python.
#The Code is adaptive to both Python2 and Python3.
#To view the simulation along with the command line arguments, please uncomment the Lines at the end.

import numpy as np

#To handle both, python2 and 3
try: input = raw_input
except NameError: pass

class Universe:

	def randomGrid(self): 
		mat = np.zeros((self.matrixSize,self.matrixSize))#np.random.choice([0,1], self.matrixSize*self.matrixSize, p=[0.2, 0.8]).reshape(self.matrixSize, self.matrixSize) 
		return np.array(mat,dtype=np.uint8)
	def addGlider(self,i, j): 
		if(self.matrixSize <  i + 3 or self.matrixSize <  j + 3 or i < 0 or j < 0):
			print("Invalid argument for Glider pattern")
			return
		glider = np.array([[0, 0, 1], 
						  [1, 0, 1], 
						  [0, 1, 1]]) 
		self.conwayMatrix[i:i+3, j:j+3] = glider

	def addBeacon(self,i,j):
		if(self.matrixSize <  i + 4 or self.matrixSize <  j + 4 or i < 0 or j < 0):
			print("Invalid argument for Beacon pattern")
			return
		beacon = np.array([[1, 1, 0, 0],
						  [1, 1, 0, 0],
						  [0, 0, 1, 1],
						  [0, 0, 1, 1]])
		self.conwayMatrix[i:i+4, j:j+4] = beacon

	def addBlinker(self,i,j):
		if(self.matrixSize <  i + 3 or i < 0 or j < 0):
			print("Invalid argument for Blinker pattern")
			return
		blinker = np.array([1, 1, 1])
		self.conwayMatrix[i,j:j+3] = blinker

	def addToad(self,i,j):
		if(self.matrixSize < j + 4 or self.matrixSize < i + 2 or i < 0 or j < 0):
			print("Invalid argument for Toad pattern")
			return
		toad =np.array([[1, 1, 1, 0],
			            [0, 1, 1, 1]])
		self.conwayMatrix[i:i+2,j:j+4] = toad

	def addUnbounded(self,i, j): 
		if(self.matrixSize < j + 5 or self.matrixSize < i + 5 or i < 0 or j < 0):
			print("Invalid argument for Unbounded pattern")
			return
		unknown = np.array([[1, 1, 1, 0, 1],
						    [1, 0, 0, 0, 0],
						    [0, 0, 0, 1, 1],
						    [0, 1, 1, 0, 1],
						    [1, 0, 1, 0, 1]]) 
		self.conwayMatrix[i:i+5, j:j+5] = unknown

	def addGosperGliderGun(self,i, j): 
	
		if(self.matrixSize < j + 38 or self.matrixSize < i + 11 or i < 0 or j < 0):
			print("Invalid argument for Gosper Glider Gun pattern")
			return

		gun = np.zeros(11*38).reshape(11, 38) 

		gun[5][1] = gun[5][2] = 1
		gun[6][1] = gun[6][2] = 1

		gun[3][13] = gun[3][14] = 1
		gun[4][12] = gun[4][16] = 1
		gun[5][11] = gun[5][17] = 1
		gun[6][11] = gun[6][15] = gun[6][17] = gun[6][18] = 1
		gun[7][11] = gun[7][17] = 1
		gun[8][12] = gun[8][16] = 1
		gun[9][13] = gun[9][14] = 1

		gun[1][25] = 1
		gun[2][23] = gun[2][25] = 1
		gun[3][21] = gun[3][22] = 1
		gun[4][21] = gun[4][22] = 1
		gun[5][21] = gun[5][22] = 1
		gun[6][23] = gun[6][25] = 1
		gun[7][25] = 1

		gun[3][35] = gun[3][36] = 1
		gun[4][35] = gun[4][36] = 1

		self.conwayMatrix[i:i+11, j:j+38] = gun 


	def update(self):
	
		nextGen = self.conwayMatrix.copy()
		total = 0
		for i in range(1,self.matrixSize-1):
			for j in range(1,self.matrixSize-1):
				total = np.sum(self.conwayMatrix[i-1:i+2,j-1:j+2])
				total = total - self.conwayMatrix[i,j]

				if  self.conwayMatrix[i,j]== 1:
					
					if (total < 2) or (total > 3):
						nextGen[i,j] = 0

				else:

					if total == 3:
						nextGen[i,j] = 1
		self.conwayMatrix[:] = nextGen.copy()


	def __init__(self, N):
		self.matrixSize = N
		self.conwayMatrix = self.randomGrid()

n = str(input("Input self.matrixSize [Minimum value= 100]: "))

def isInt(s):
	try:
		s = int(s)
		return True
	except ValueError as e:
		return False
while(not isInt(n) or int(n) < 100):
	n = input("Please enter a valid integer. :  ")

CM = Universe(int(n))

print("Do you want add any of the following to the Grid- \n1) Glider \n2) Gosper Glider Gun \n3) Beacon pattern \n4) Blinker pattern \n5) Toad pattern \n6) Unbounded \n ")
choices = str(input("Please enter list of options you want to add , seperated by comma. viz 2,4,6 :  "))
choices = np.array(choices.split(','),dtype = np.uint8)
available_functions = [CM.addGlider,CM.addGosperGliderGun,CM.addBeacon,CM.addBlinker,CM.addToad,CM.addUnbounded]
available_patterns = {1:"Glider",2: "Gosper Glider Gun",3: "Beacon Pattern",4: "Blinker Pattern",5: "Toad Pattern",6:"Unbounded pattern"}

for c in choices:
	x,y = CM.matrixSize//2,CM.matrixSize//2
	while(True):
		inp = str(input("Input x and y position for "+available_patterns[c]+" pattern seperated by \',\' ")).split(',')
		if(len(inp) != 2):
			print("Please enter 2 values.")
		else:
			x,y = inp
			break
	if(isInt(x) and isInt(y)):
		available_functions[c-1](int(y),int(x))
	else:
		print("Invalid arguments")



#The lines below can be used to simulate the code on OpenCV

import time 
import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)

old = CM.conwayMatrix[:]
for i in range(1000):
	cv2.imshow('img',CM.conwayMatrix[:] * 255)
	cv2.waitKey(10)
	CM.update()
	print(np.mean(np.abs(old-CM.conwayMatrix[:])))

cv2.destroyAllWindows()
