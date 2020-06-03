import sys

def depthFirstRec (grid, x, y, curPath):
	global columns, lines, iteractions

	iteractions +=1
	curPath.append([x,y])
	# print(curPath)
	
	if grid[x][y] == "$":
		with open(filename, 'a') as f:
			f.write(str(iteractions) + '\n')
			f.write(str(curPath))
		return True

	grid[x][y] = 'X' # mark as explored so it won't loop

	if x<lines-1 and grid[x+1][y] in ['*', '$'] and  [x+1,y] not in curPath and depthFirstRec(grid, x+1, y, curPath):
		return True

	elif y<columns-1 and grid[x][y+1] in ['*', '$'] and [x,y+1] not in curPath and depthFirstRec(grid, x, y+1, curPath):
		return True

	elif x>0 and grid[x-1][y] in ['*', '$'] and [x-1,y] not in curPath and depthFirstRec(grid, x-1, y, curPath):
			return True

	if y>0 and grid[x][y-1] in ['*', '$'] and [x,y-1] not in curPath and depthFirstRec(grid, x, y-1, curPath):
		return True 

	else:
		grid[x][y] = '*'
		curPath.pop()
		return False

def depthFirst (inputFile, grid, start):
	global lines, columns, iteractions, filename
	lines = len (grid)
	columns = len (grid[0])
	iteractions = 0
	filename = inputFile + '_depthFirst.out'

	return depthFirstRec(grid, start[0], start[1], [])