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
		# No points, I lose
		# Check what I choose
		if opp == 'A': # Opp = Rock
			# I choose scissors
			points += 3
		elif opp == 'B': # Opp = Paper
			# I choose rock
			points += 1
		elif opp == 'C': # Opp = scissors
			# I choose paper
			points += 2
		else:
			print('error')
			sys.exit()
	elif me == 'Y':
		# I draw
		points += 3
		# Check what I choose
		if opp == 'A': # Opp = Rock
			# I choose rock
			points += 1
		elif opp == 'B': # Opp = Paper
			# I choose paper
			points += 2
		elif opp == 'C': # Opp = scissors
			# I choose scissors
			points += 3
		else:
			print('error')
			sys.exit()
	elif me == 'Z':
		# I win
		points += 6
		# Check what I choose
		if opp == 'A': # Opp = Rock
			# I choose 
			points += 2
		elif opp == 'B': # Opp = Paper
			# I choose scissors
			points += 3
		elif opp == 'C': # Opp = scissors
			# I choose rock
			points += 1
		else:
			print('error')
			sys.exit()
	else:
		print('error')
		sys.exit()

# Print output data
print(points)

