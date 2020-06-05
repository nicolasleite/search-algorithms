#!/bin/bash

for file in examples/*.in; do
	python3 src/main.py $file
done

