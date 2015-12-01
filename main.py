my_pick_array = [];

for x in range(2,28):
	my_pick_array.append([x,""])

def win_chance(my_pick):
    
    my_wins = 0

    for random_pick in range(2,28):
        # Is this the right way to deal with Draws?
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

    return my_wins

for x in range(2,28):
	my_pick_array[x-2][1] = win_chance(x)

print my_pick_array

def sort_by_prob(s):
    return s[1]

print sorted(my_pick_array, key=sort_by_prob, reverse=True)