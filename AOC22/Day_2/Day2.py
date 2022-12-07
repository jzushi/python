# Day Two: Rock, Paper, Scissors

# Read in input file with RPS strategy
f = open("input.txt", "r")
lines = f.readlines()
rounds = [entry.strip() for entry in lines]

input_shapes = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
shape_points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
outcome_points = {'Lose': 0, 'Draw': 3, 'Win': 6}

def round_points(round_string):
    opponent_shape = input_shapes[round_string[0]]
    our_shape = input_shapes[round_string[2]]

    if opponent_shape == our_shape:
        return outcome_points['Draw'] + shape_points[our_shape]
    elif (opponent_shape, our_shape) in [('Paper', 'Rock'), ('Rock', 'Scissors'), ('Scissors', 'Paper')]:
        return outcome_points['Lose'] + shape_points[our_shape]
    else:
        return outcome_points['Win'] + shape_points[our_shape]


print(sum([round_points(round_string) for round_string in rounds]))


# part two
input_shapes = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
shape_points = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
outcome_points = {'Lose': 0, 'Draw': 3, 'Win': 6}

def round2_points(round_string):
    opponent_move = input_shapes[round_string[0]]
    our_move = input_shapes[round_string[2]]

    if (opponent_move, our_move) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
        return outcome_points[our_move] + shape_points['Rock']
    elif (opponent_move, our_move) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
        return outcome_points[our_move] + shape_points['Paper']
    else:
        return outcome_points[our_move] + shape_points['Scissors']

print(sum([round2_points(round_string) for round_string in rounds]))