'''
	consider:
	hand: 12345
	detectes: 12345, 2345. 345
	but not 123, 234
	
'''

def findRun(cards):
	'''
	print ('this is the list that was recv\'d')
	print ('--------------------------------')
	print (cards)
	'''
	
	# copy list
	import copy
	cardsCopy = copy.deepcopy(cards)
	
	# must at the high end ace to detect QKA run
	for card in cardsCopy:
		if card[0] == 0: cardsCopy.append([13, card[1]])
	
	# sort by value, then sort by suit
	cardsCopy.sort()
	cardsCopy.sort(key=lambda x: x[1])
	'''
	print ('this is a copy sorted by value then suit')
	print ('------------------------------')
	print (cardsCopy)
	'''
	
	runsHolder = []
	runsCount = 0
	for i in range(len(cardsCopy)):
		runCounter = 0
		for x in range(i, len(cardsCopy)-1):
		
			#print ('checking ' + str(cardsCopy[x]) + ' and ' + str(cardsCopy[x+1]))
			if cardsCopy[x][0] + 1 == cardsCopy[x+1][0] and cardsCopy[x][1] == cardsCopy[x+1][1]:
				# then there's 2 cards that will work, increase x and go again
				runCounter = runCounter + 1
			else: break	
		
		if runCounter>1: # then we have a run
			#print ('run found starting at ' + str(cardsCopy[i]) + ' and ending at ' + str(cardsCopy[i+runCounter]))
			tList = []
			for z in range(runCounter+1):
				tList.append(cardsCopy[i+z])
			runsHolder.append(tList)
			
			runsCount = runsCount + 1
	
	# set 13 back to 0
	for run in runsHolder:
		for card in run:
			if card[0] == 13:
				card[0] = 0
				
	return runsHolder	
	'''		
	# error checking
	if runsCount != 7:
		print ('DID NOT FIND 7 RUNS')
		exit()
	'''

				
myHand = [[11, 's'], [0, 's'], [10, 'd'], [11, 'd'], [4, 'h'], [12, 'c'], [1, 'h'], [2, 'h'], [3, 'h'], [9, 'd'], [8, 'c'], [7, 'h'], [5, 'd'], [5, 'c'], [5, 's'], [5, 'h'], [12, 's'], [12, 'h'], [12, 'd']]

import random
for i in range(1):
	random.shuffle(myHand)
	
	runs = findRun(myHand)
	for run in runs:
		print(run)







