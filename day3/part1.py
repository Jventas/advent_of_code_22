# Imports
import sys
import string

# Read input data
data = open('input.txt','r')
lines = data.read().split('\n')
# Remove blanks
lines.remove('')

# Solve the problem
char_to_prior = list(string.ascii_lowercase + string.ascii_uppercase)
char_to_prior.insert(0,'')

points = 0
for line in lines:
	# Number of elements
	n_el = len(line)
	# Splitting point
	cut = int(n_el*0.5)
	# Two compartments
	comp1 = line[0:cut]
	comp2 = line[cut:]
	for item in comp1:
		if item in comp2:
			points += char_to_prior.index(item)
			break

# Print output data
print(points)

