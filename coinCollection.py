'''
Author: Jorge Bautista
Description: Implemntation of the coin collection problem found in Algorithims Design and Analysis
						 Using Dynamic Programming
Date: Dec 13, 2018
'''

def inBounds(i,j,m,n):
	return False if i == m or j == n else True

def findMax(i,j,arr,total):
	if not inBounds(i,j,len(arr), len(arr[0])):
		return total

	if arr[i][j] == 1:
		total += 1

	return max(findMax(i + 1,j,arr ,total), findMax(i,j+1,arr,total))

arr = [ [0]*5 for i in range(4)]
arr[2][3] = 1
arr[3][3] = 1
arr[1][2] = 1
arr[3][3] = 1
arr[0][2] = 1
arr[1][0] = 1
arr[1][4] = 1

for i in range(4):
	for j in range(5):
		print(arr[i][j], end='')
	print()

print(findMax(0,0,arr,0))
