import sys

def breadthFirst(inputFile, grid, start):
	iteractions = 1
	lines = len (grid)
	columns = len (grid[0])
	filename = inputFile + '_breadthFirst.out'

	queue = []
	queue.append(start)

	while queue:
		iteractions += 1

		path = queue.pop(0)
		try:
			[x,y] = path[-1]
		except Exception:
			path = [path]
			[x,y] = path[-1]

		if grid[x][y] == '$':
			with open(filename, 'a') as f:
				f.write(str(iteractions) + '\n')
				f.write(str(path))
			print ("BFS finished successfully")
			return True

		grid[x][y] = 'X' # mark as explored so it won't loop

		if x<lines-1 and grid[x+1][y] in ['*', '$']:
			new_path = list(path)
			new_path.append([x+1,y])
			queue.append(new_path)
		if y<columns-1 and grid[x][y+1] in ['*', '$']:
			new_path = list(path)
			new_path.append([x,y+1])
			queue.append(new_path)
		if x>0 and grid[x-1][y] in ['*', '$']:
			new_path = list(path)
			new_path.append([x-1,y])
			queue.append(new_path)
		if y>0 and grid[x][y-1] in ['*', '$']:
			new_path = list(path)
			new_path.append([x,y-1])
			queue.append(new_path)

	return False

	# if curLevel < level:
		# if x<lines-1 and grid[x+1][y] in ['*', '$']:
		# 	newPath = breadthFirstRec(grid, x+1, y, curLevel+1,curPath)
		# 	if newPath:
		# 		return True
		# 	else:
		# 		curPath.pop()
		# if y<columns-1 and grid[x][y+1] in ['*', '$']:
		# 	newPath = breadthFirstRec(grid, x, y+1, curLevel+1,curPath)
		# 	if newPath:
		# 		return True
		# 	else:
		# 		curPath.pop()
		# if x>0 and grid[x-1][y] in ['*', '$']:
		# 	newPath = breadthFirstRec(grid, x-1, y, curLevel+1,curPath)
		# 	if newPath:
		# 		return True
		# 	else:
		# 		curPath.pop()
		# if y>0 and grid[x][y-1] in ['*', '$']:
		# 	newPath = breadthFirstRec(grid, x, y-1, curLevel+1,curPath)
		# 	if newPath:
		# 		return True 
		# 	else:
		# 		curPath.pop()

	# grid[x][y] = '*'
	# if curLevel == 0:
	# 	level += 1
	# 	breadthFirstRec(grid, x, y, 0, [])
	# else:
	# 	return False

# def breadthFirst(inputFile, grid, start):
# 	global level, lines, columns, iteractions, filename
	

# 	return breadthFirstRec (grid, start[0], start[1], 0, [])