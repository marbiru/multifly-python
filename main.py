my_pick_list = []

for x in range(2,28):
	my_pick_list.append([x,"",""])

random_pick_list = []

for x in range(2,28):
    random_pick_list.append(x)

my_previous_moves = []
computers_previous_moves = []

def win_chance(my_pick):
    
    my_wins = 0

    for random_pick in random_pick_list:
        if random_pick == my_pick:
        	my_wins += 0.5
        elif random_pick % my_pick == 0:
            my_wins += 0
        elif my_pick % random_pick == 0:
        	my_wins += 1
        elif my_pick < random_pick:
        	my_wins += 1
        elif random_pick < my_pick:
        	my_wins += 0

    win_fraction = float(my_wins)/len(random_pick_list)

    return win_fraction

for x in range(2,28):
    my_pick_list[x-2][2] = win_chance(x)

def calculate_probabilities():

    for x in range(2,len(my_pick_list)+2):
       difference_from_baseline = win_chance(x) - my_pick_list[x-2][2]
       my_pick_list[x-2][1] = round(difference_from_baseline, 2)

    def sort_by_prob(s):
        return s[1]

    my_pick_list_sorted = sorted(my_pick_list, key=sort_by_prob, reverse=True)

    print "\n Your next move:"
    print my_pick_list_sorted[0][:-1]
    print "\n Your previous moves:"
    print my_previous_moves
    print "\n Computer's previous moves:"
    print computers_previous_moves
    print "\n Other options had differentials:"
    print my_pick_list_sorted[1:]

    my_previous_moves.append(my_pick_list_sorted[0][0])

    my_pick_list.pop(0)

def computers_move():

    user_input = int(raw_input('\nWhat number did the computer play?\n'))

    if user_input in computers_previous_moves:
         user_input = int(raw_input('\nYou\'ve entered that previously! What number did the computer play this time?\n'))
    elif user_input in range(2,27):
        return user_input
    else: 
        user_input = int(raw_input('\nThat doesn\'t seem right. What number did the computer play?\n'))
    
    computers_previous_moves.append(user_input)

    computers_last_move = random_pick_list.index(user_input)

    random_pick_list.pop(computers_last_move)

def main_function():
    calculate_probabilities()
    computers_move()
    main_function()

print "\nWelcome to the Multifly Solver. The following list shows the current differential between each pick's baseline win-chance and current win-chance. Always choose the first number on the list as your next move -- the other options/probabilities are shown just for interest. Then, after each round, input what the computer just played and the Solver will recalculate probabilities. \n"

main_function()