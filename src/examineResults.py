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

mediumIt=[0,0]
mediumLen=[0,0]
resultsTable=PrettyTable()
resultsTable.title='Obtained results'
resultsTable.field_names=['File', 'Iteractions', 'Lenght']
for item in resList:
	if re.search('(breadth.*)', item[0]):
		mediumIt[0] += item[1]
		mediumLen[0] += item[2]
	elif re.search('(depth.*)', item[0]):
		mediumIt[1] += item[1]
		mediumLen[1] += item[2]
	
	resultsTable.add_row(item)

for i in range(0, 2):
	mediumIt[i] = mediumIt[i]/len(resList)/2
	mediumLen[i] = mediumLen[i]/len(resList)/2


mediumTable=PrettyTable()
mediumTable.title='Medium of Results'
mediumTable.field_names=['Algorithm', 'Iteractions', 'Lenghts']
mediumTable.add_row(['Breadth First Search', mediumIt[0], mediumLen[0]])
mediumTable.add_row(['Depth First Search', mediumIt[1], mediumLen[1]])

print()
print('########################################')
print('########## Summary of results ##########')
print('########################################')
print()

print (resultsTable)
print (mediumTable)