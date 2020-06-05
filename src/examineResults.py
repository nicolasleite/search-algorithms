import os
import sys
import re
import glob
from prettytable import PrettyTable

folder = os.getcwd() + '/' + sys.argv[1]

allFiles =  glob.glob(os.path.join(folder, '*.out'))

resList=[]
for filename in allFiles:
	with open(filename) as file:
		lines = file.readlines()
		iteractions = int (lines[0].rstrip())
		lenght = int (lines[1])
		resList.append([filename.split('examples/')[1], iteractions, lenght])

results=PrettyTable(['File', 'Iteractions', 'Lenght'])
for item in resList:
	results.add_row(item)
print (results)
