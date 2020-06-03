import sys

def breadthFirstRec(grid, x, y, curLevel, curPath):
	global level, columns, lines, iteractions

	iteractions +=1
	curPath.append([x,y])
	
	if grid[x][y] == "$":
		with open(filename, 'a') as f:
			f.write(str(iteractions) + '\n')
			f.write(str(curPath))
		return True

	grid[x][y] = 'X' # mark as explored so it won't loop

	if curLevel < level:
		if x<lines-1 and grid[x+1][y] in ['*', '$'] and  [x+1,y] not in curPath:
			newPath = breadthFirstRec(grid, x+1, y, curLevel+1,curPath)
			if newPath:
				return True
			else:
				curPath.pop()
		if y<columns-1 and grid[x][y+1] in ['*', '$'] and [x,y+1] not in curPath:
			newPath = breadthFirstRec(grid, x, y+1, curLevel+1,curPath)
			if newPath:
				return True
			else:
				curPath.pop()
		if x>0 and grid[x-1][y] in ['*', '$'] and [x-1,y] not in curPath:
			newPath = breadthFirstRec(grid, x-1, y, curLevel+1,curPath)
			if newPath:
				return True
			else:
				curPath.pop()
		if y>0 and grid[x][y-1] in ['*', '$'] and [x,y-1] not in curPath:
			newPath = breadthFirstRec(grid, x, y-1, curLevel+1,curPath)
			if newPath:
				return True 
			else:
				curPath.pop()

	grid[x][y] = '*'
	if curLevel == 0:
		level += 1
		breadthFirstRec(grid, x, y, 0, [])
	else:
		return False

def breadthFirst(inputFile, grid, start):
	global level, lines, columns, iteractions, filename
	lines = len (grid)
	columns = len (grid[0])
	level = 1
	iteractions = 0
	filename = inputFile + '_breadthFirst.out'

	return breadthFirstRec (grid, start[0], start[1], 0, [])