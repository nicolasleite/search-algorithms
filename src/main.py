from readGrid import readGrid 
from breadthFirst import breadthFirst
from depthFirst import depthFirst
import sys
import copy

def clearGrid (grid):
	for line in grid:
		for element in line:
			if element == 'X':
				element = '*'


def main():
	filename = str(sys.argv[1])
	inp = readGrid (filename)

	start = inp[1]
	finish = inp[2]

	print ("Running Depth-First Search...")
	grid = copy.deepcopy(inp[0])
	depthFirst (filename, grid, start)

	print ("Running Breadth-First Search...")
	grid = copy.deepcopy(inp[0])
	breadthFirst (filename, grid, start)

	# analizeResults ([dfs, bfs])
	return

if __name__ == "__main__":
	main()
try:
	pass
except Exception as e:
	raise e