# Imports
import sys

# Read input data
data = open('input.txt','r')
lines = data.read().split('\n')
# Remove blanks
lines.remove('')
# Solve the problem
points = 0
for line in lines:
	line = line.strip().split()
	me = line[1]
	opp = line[0]
	if me == 'X':
		# Add points for chosing rock
		points += 1
		# Check opponent
		if opp == 'A':
			# Draw
			points += 3
		elif opp == 'B':
			# I lose
			pass
		elif opp == 'C':
			# I win
			points += 6
		else:
			print('error')
			sys.exit()
	elif me == 'Y':
		# Add points for chosing paper
		points += 2
		# Check opponent
		if opp == 'A':
			# I win
			points += 6
		elif opp == 'B':
			# Draw
			points += 3
		elif opp == 'C':
			# I lose
			pass
		else:
			print('error')
			sys.exit()
	elif me == 'Z':
		# Add points for chosing scissors
		points += 3
		# Check opponent
		if opp == 'A':
			# I lose
			pass
		elif opp == 'B':
			# I win
			points += 6
		elif opp == 'C':
			# Draw
			points += 3
		else:
			print('error')
			sys.exit()
	else:
		print('error')
		sys.exit()

# Print output data
print(points)

