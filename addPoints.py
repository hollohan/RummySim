# takes a list of cards and returns sum of points
# 0      = A      = 5, 20
# 1-8    = 2-9    = 5
# 9-12  = 10,JQK  = 10
# 13     = A      = 15



def addPoints (hand):
	handValue = 0
	for card in hand:
		if card[0] == 0:
			if hand[0][0] == hand[1][0]:
				handValue = handValue + 20
			elif card == hand[2]:
				handValue = handValue + 15
			else:
				handValue = handValue + 5
		elif card[0] > 0 and card[0] < 9: handValue = handValue + 5
		elif card[0] > 8 and card[0] < 13: handValue = handValue + 10
		elif card[0] == 13: # must be run
			handValue = handValue + 15
				
	return handValue
'''	
hands = [  [[0, 'h'], [1, 'h'], [2, 'h']], 
				[[4, 'h'], [4, 'c'], [4, 's']],
				[[11, 's'], [12, 's'], [0, 's']],
				[[0, 'h'], [0, 'h'], [0, 'h'], [0, 'h']],
				[[7, 'h'], [8, 'h'], [9, 'h']]	]
			
for hand in hands:
	result = addPoints(hand)
	print (str(hand) + ' = ' + str(result))
'''

