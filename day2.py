f = open("day_2_input.txt", "r")


point_allocations = {
    ('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'):3,
    ('A', 'Y'): 6, ('B', 'Z'): 6, ('C', 'X'):6,
    ('A', 'Z'): 0, ('B', 'X'): 0, ('C', 'Y'):0
}

desired_play = {
    ('A', 'X'): 'Z', ('B', 'Y'): 'Y', ('C', 'Z'):'X',
    ('A', 'Y'): 'X', ('B', 'Z'): 'Z', ('C', 'X'):'Y',
    ('A', 'Z'): 'Y', ('B', 'X'): 'X', ('C', 'Y'):'Z'
}

def first_challenge():
	total_score = 0
	for x in f:
		x = x.split()  # Split the line into columns
		opponent_move = x[0]
		your_move = x[1]
		
		line_score = point_allocations[(opponent_move, your_move)]  # Get the score from the dictionary
		line_score += {'X': 1, 'Y': 2, 'Z': 3}[your_move]  # Add points based on your move
		
		total_score += line_score

	print(total_score)
def second_challenge():
	total_score = 0
	for x in f:
		x = x.split()  # Split the line into columns
		opponent_move = x[0]
		your_outcome = x[1]
		line_score = {'X': 0, "Y": 3, "Z": 6}[your_outcome]
		
		your_move = desired_play[(opponent_move, your_outcome)]  # Get the score from the dictionary
		line_score += {'X': 1, 'Y': 2, 'Z': 3}[your_move]  # Add points based on your move
		
		total_score += line_score

	print(total_score)

if __name__ == "__main__":
    # first_challenge()
	second_challenge()