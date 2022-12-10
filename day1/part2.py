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


N_reind = 3
max_cal = 0
for ii in range(N_reind):
	max_i = max(reindeers)
	max_cal += max_i
	reindeers.remove(max_i)

# Print output data
print(max_cal)

