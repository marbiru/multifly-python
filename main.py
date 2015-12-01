myPickArray = [];

for x in range(2,27):
	myPickArray.append(x)

print myPickArray

def win_chance(myPick):
    
    myWins = 0

    for randomPick in range(2,28):
        # Is this the right way to deal with Draws?
        if randomPick == myPick:
        	myWins += 0.5
        elif randomPick % myPick == 0:
            myWins += 0
        elif myPick % randomPick == 0:
        	myWins += 1
        elif myPick < randomPick:
        	myWins += 1
        elif randomPick < myPick:
        	myWins += 0

    return myWins

print win_chance(2)