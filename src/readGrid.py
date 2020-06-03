def readGrid (inputFile):
	with open(inputFile) as file:
		firstLine = file.readline()
		
		size = firstLine.split()
		size[0] = int (size[0])
		size[1] = int (size[1])
		
		grid = []
		
		for i in range(0, size[0]):
			line=[]
			for j in range(0, size[1]):
				char = file.read(1)
				if (char == '\n'):
					char = file.read(1)
				line.append(char)
				if char == '#':
					start = [i,j]
				elif char == '$':
					finish = [i,j]
			grid.append(line)

	return [grid, start, finish]