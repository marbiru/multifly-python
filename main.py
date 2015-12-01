my_pick_array = [];

for x in range(2,28):
	my_pick_array.append([x,""])

random_pick_array = []

for x in range(2,28):
    random_pick_array.append(x)

def win_chance(my_pick):
    
    my_wins = 0

    #instead of "range" this needs to use an array as its input and we pop
    for random_pick in random_pick_array:
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

def sort_by_prob(s):
    return s[1]

my_pick_array_sorted = sorted(my_pick_array, key=sort_by_prob, reverse=True)

print my_pick_array_sorted

computer_played = int(raw_input('Computer played [number]?\n'))

random_pick_array.pop(computer_played - 2)

print random_pick_array

for x in range(2,28):
    my_pick_array[x-2][1] = win_chance(x)

def sort_by_prob(s):
    return s[1]

my_pick_array_sorted = sorted(my_pick_array, key=sort_by_prob, reverse=True)

print my_pick_array_sorted

