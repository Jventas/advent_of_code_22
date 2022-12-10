# Imports
import sys

# Read input data
data = open('input.txt','r')
lines = data.read().split('\n')

# Solve the problem
reindeers = []
calories = 0
for line in lines:
	if line != '':
		calories += float(line)
	else:
		reindeers.append(calories)
		calories = 0
max_cal = max(reindeers)

# Print output data
print(max_cal)

