
#This program outputs a magic square based on the odd number entered by the user.

import numpy as np
import math
import os

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")
#nt is a window check, if you are on window use cls, else clear(Mac)

checker = True
moveUp = 1
moveRight = 1


#To check to see if a odd number was enter, if not try again
matrix_size = int(input("Enter the size of the Matrix. It must be an Odd-numbered matrix: "))
n = matrix_size
while(checker):
	if(matrix_size == 1):
		matrix_size = int(input("Try Again. Please enter an Odd number: "))
	elif(matrix_size % 2) == 1:
		checker = False
	else:
		matrix_size = int(input("Try Again. Please enter an Odd number: "))
clear_screen()
print("Matrix Size: ",matrix_size,'x',matrix_size)

matrixEmp = np.zeros((matrix_size, matrix_size), dtype=int)
#for i in range(matrix_size):
#	for j in range(matrix_size):
#		matrixEmp[i][j] = 0

print("")

#The number the Metrix should equal, all sides.
ResultNum = n*((n*n +1)/2)
print("The following Matrix equals ",int(ResultNum), " on all sides.")

print("")


def XposChecker(x):
	if x == n: #matrix size will not go n start at 0, not 1
		x = 0 #Example, if n = 3 then this is out of bounds, highest is 2 in a 3x3
	elif x == -1:
		x = (n-1)#Example, if n = 0, then -1 makes is an error, must be 3 - 1 to get to other side.

	return x

def YposChecker(y):
	if y == n: #matrix will not go n start at 0, not 1
		y = 0
	elif y == -1:
		y = (n-1)

	return y


posCounter = 1 #This counter will add the numbers into the matrix
MaxPosCount = n * n #The number of indexes
XPos = 0 # X Position
YPos = 0 # Y Position

for i in range(MaxPosCount):
	if posCounter == 1:#The starting number you have to use is 1
		XPos = 0
		YPos = math.floor(n/2) #This makes sure the 1 is in the top-middle row; always.
		matrixEmp[XPos][YPos] = posCounter #This should always output 1
	elif posCounter > 1:
		XPos -=1 #This is moving up
		YPos +=1 #This is moving right
		XPos = XposChecker(XPos)
		YPos = YposChecker(YPos)

		if matrixEmp[XPos][YPos] != 0: #If a number is filled in.
			XPos += 1 #Going back to initial spot
			YPos -= 1 #Going back to initial spot
			
			XPos = XposChecker(XPos)
			YPos = YposChecker(YPos)

			XPos += 1 #Going beneath the initial spot
			
			matrixEmp[XPos][YPos] = posCounter

		else:
			matrixEmp[XPos][YPos] = posCounter

	posCounter +=1

print(np.array(matrixEmp))