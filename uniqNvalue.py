# takes a list of hands
# returns most valuable unique (not containing the same cards as another hand) hands
from addPoints import addPoints
from random import shuffle

def uniqNvalue(hands):
	
	from itertools import permutations
	perms = permutations(hands)
	results = []
	for perm in perms:
		uniHands = []
		for hand in perm:
			alreadyThere = 0
			for card in hand:
				for uh in uniHands:
					if card in uh:
						alreadyThere = 1
			if not alreadyThere:
				uniHands.append(hand)
		if uniHands not in results:
			results.append(uniHands)
	
	highestScore = 0
	newResults = []
	for res in results:
			points = 0
			for hand in res:
					points = points + addPoints(hand)
			newResults.append([points, res])
			if points > highestScore:
				highestScore = points
				
	results = []	
	for thing in newResults:
		if thing[0] == highestScore:
			results.append(thing[1])
	
	# if there's duplicate entried, this is not completely random
	shuffle(results)
	return results[0]

	
	
	
			

'''
hands = [   [[0, 'h'], [1, 'h'], [2, 'h'], [3, 'h']],
				[[0, 'h'], [1, 'h'], [2, 'h']],
				[[1, 'h'], [2, 'h'], [3, 'h']],
				[[3, 'h'], [3, 's'], [3, 'd']],
				[[0, 'h'], [0, 's'], [0, 'c']]	]
				

results = uniqNvalue(hands)

for res in results:
	print (res)
	print ('')
'''




