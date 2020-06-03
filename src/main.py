from readGrid import readGrid 
from breadthFirst import breadthFirst
from depthFirst import depthFirst
import sys

def main():
	filename = str(sys.argv[1])
	inp = readGrid (filename)

	grid = inp[0]
	start = inp[1]
	finish = inp[2]

	print ("Running Depth-First Search...")
	dfs = depthFirst (filename, grid, start)
	# print ("Running Breadth-First Search...")
	# bfs = breadthFirst (filename, grid, start)
	

	# analizeResults ([dfs, bfs])
	return

if __name__ == "__main__":
	main()
