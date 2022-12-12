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
for ii in range(0,len(lines),3):
	# Read lines
	line1 = lines[ii]
	line2 = lines[ii+1]
	line3 = lines[ii+2]
	# Check which character is common to the three
	for item in line1:
		if item in line2 and item in line3:
			points += char_to_prior.index(item)
			break

# Print output data
print(points)

