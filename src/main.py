from readGrid import readGrid 
from breadthFirst import breadthFirst
from depthFirst import depthFirst
import sys
import copy

def main():

	filename = str(sys.argv.pop(1))
	inp = readGrid (filename)

	start = inp[1]
	finish = inp[2]

	print ("Running Depth-First Search...")
	grid = copy.deepcopy(inp[0])
	depthFirst (filename, grid, start)

	print ("Running Breadth-First Search...")
	grid = copy.deepcopy(inp[0])
	breadthFirst (filename, grid, start)

	return

if __name__ == "__main__":
	main()
