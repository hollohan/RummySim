# function takes a list of cards and returns all possible quads

def findQuads(cards):
	'''
	print ('this is the list that was recv\'d')
	print ('--------------------------------')
	print (cards)
	'''
	import copy
	cardsCopy = copy.deepcopy(cards)
	
	cardsCopy.sort()
	'''
	print ('this is a copy sorted by value')
	print ('------------------------------')
	print (cardsCopy)
	'''
	
	quadsCount = 0
	quadsHolder = []
	for i in range(len(cardsCopy)-3):
		if cardsCopy[i][0] == cardsCopy[i+1][0] == cardsCopy[i+2][0] == cardsCopy[i+3][0]:	# then we have quads
			# load cards into vars
			first  = cardsCopy[i][0]
			second = cardsCopy[i+1][0]
			third  = cardsCopy[i+2][0]
			fourth = cardsCopy[i+3][0]
			
			quadsHolder.append([first, second, third, fourth])
			'''
			print ('quads have been found')
			print ('---------------------')
			print (str(first) + ' ' + str(second) + ' ' + str(third) + ' ' + str(fourth))
			'''
			quadsCount = quadsCount + 1
	'''		
	#summary
	print (str(quadsCount) + ' sets of quads found')
	# error test
	if quadsCount != 2:
		print (' - 2 SETS OF QUADS NOT DETECTED - ')
		exit()
	'''
	return quadsHolder
			
myHand = [[12, 'c'], [1, 'h'], [2, 'h'], [3, 'h'], [9, 'd'], [8, 'c'], [7, 'h'], [5, 'd'], [5, 'c'], [5, 's'], [5, 'h'], [12, 's'], [12, 'h'], [12, 'd']]

import random
for i in range(1):
	random.shuffle(myHand)
	quads = findQuads(myHand)
	for quad in quads:
		print (quad)






