# function takes a list of cards and returns all possible trips
# suits h, d, c, s
def findTrips(cards):
	'''
	print ('this is the list that was recv\'d')
	print ('--------------------------------')
	print (cards)
	'''
	import copy
	cardsCopy = copy.deepcopy(cards)
	
	# test for 3 of a kind
	cardsCopy.sort()
	'''
	print ('this is a copy sorted by value')
	print ('------------------------------')
	print (cardsCopy)
	'''
	
	tripsCount = 0
	tripsHolder = []
	for i in range(len(cardsCopy)-2):
		if cardsCopy[i][0] == cardsCopy[i+1][0] == cardsCopy[i+2][0]:	# then there's def trips
			# load each card to var
			first  = cardsCopy[i]
			second = cardsCopy[i+1]
			third  = cardsCopy[i+2]
			
			tripsHolder.append([first, second, third])
			'''
			print ('trips have been found')
			print ('---------------------')
			print (str(first) + ' ' + str(second) + ' ' + str(third))
			'''
			tripsCount = tripsCount + 1
			
	# summary
	#print (str(tripsCount) + ' sets of trips found')
	'''
	# error test
	if tripsCount != 3:
		print (' - 3 SETS OF TRIPS NOT DETECTED - ')
		exit()
	'''
	
	return tripsHolder
	
'''
myHand = [[1, 'h'], [2, 'h'], [3, 'h'], [9, 'd'], [8, 'c'], [7, 'h'], [5, 'd'], [5, 'c'], [5, 's'], [5, 'h'], [12, 's'], [12, 'h'], [12, 'd']]

for i in range(1):
	import random
	random.shuffle(myHand)
	trips = findTrips(myHand)
	for trip in trips:
		print (trip)
'''
	
	
	
	
	
	
	
	
	
