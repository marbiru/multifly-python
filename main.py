my_pick_list = [];

for x in range(2,28):
	my_pick_list.append([x,""])

random_pick_list = []

for x in range(2,28):
    random_pick_list.append(x)

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

    win_fraction = round(win_fraction, 2)
    
    return win_fraction

def calculate_probabilities():

    for x in range(2,28):
       my_pick_list[x-2][1] = win_chance(x)

    def sort_by_prob(s):
        return s[1]

    my_pick_list_sorted = sorted(my_pick_list, key=sort_by_prob, reverse=True)

    print my_pick_list_sorted

def computers_move():

    user_input = int(raw_input('Computer played [number]?\n'))
      
    computers_last_move = random_pick_list.index(user_input)

    random_pick_list.pop(computers_last_move)

def main_function():
    calculate_probabilities()
    computers_move()
    main_function()

main_function()