#!/bin/bash

# Cleaning up old output files
rm examples/*.out

# Running the algorithms in different mazes
for file in examples/*.in; do
	python3 src/main.py $file
done

# Examining the results
python3 src/examineResults.py examples

