from readGrid import readGrid 
from breadthFirst import breadthFirst
from depthFirst import depthFirst
import sys
import copy

def main():

	sys.argv.pop(0)  # removing main.py from argv
	for filename in sys.argv:
		filename = str(sys.argv.pop())
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
