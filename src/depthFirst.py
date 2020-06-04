import sys

def depthFirst (inputFile, grid, start):
	curPath = [start]
	lines = len (grid)
	columns = len (grid[0])
	iteractions = 1
	filename = inputFile + '_depthFirst.out'
	x = start[0]
	y = start[1]

	while grid[x][y] != "$":
		iteractions +=1

		grid[x][y] = 'X' # mark as explored so it won't loop

		if x<lines-1 and grid[x+1][y] in ['*', '$']:
			x=x+1

		elif y<columns-1 and grid[x][y+1] in ['*', '$']:
			y=y+1

		elif x>0 and grid[x-1][y] in ['*', '$']:
			x=x-1

		elif y>0 and grid[x][y-1] in ['*', '$']:
			y=y-1

		else:
			[x,y] = curPath.pop()
			continue
		
		curPath.append([x,y])

	#end while


	curPath.append([x,y])
	with open(filename, 'a') as f:
		f.write(str(iteractions) + '\n')
		f.write(str(curPath))
	print ("DFS finished successfully")
	return True
