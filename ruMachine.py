from Player import Player
print ('\n\n')


# create deck/board
deck = []
board = []
suits = ['h', 'd', 's', 'c']
for suit in suits:
	[deck.append([z, suit]) for z in range(13)]
print (deck)
print ("--- " + str(len(deck)) + " cards in the deck ---")
print ('\n\n')



# shuffle the deck
import random
random.shuffle(deck)
print (deck)
print (' ----- Shuffled Deck -----')
print ('\n\n')



# create players
x=4									# number of players
players = []
for i in range(x):
	newPlayer = Player(i)
	players.append(newPlayer)
	print ('Player#: ' + str(i))
print ('------- Players -------')
print ('\n\n')



# deal 7 cards to each player
for i in range(7):
	for player in players:
		player.hand.append(deck.pop())
for player in players:
	print ('%i: %s' % (player.id, str(player.hand)))
print ('----- Cards Dealt -----')
print ('\n\n')

# put one card on the board
board.append(deck.pop())


print ('-'*30 + 'Let The Games Begin' + '-'*30)
print('\n\n')


# run turns
for i in range(10):

	print ('\n\nthe board')
	print ('---------')
	print (board)
	print ('\n')

	players[0].turn(board, deck)

print('\n')
print ('final score')
print ('-----------')
for player in players:
	print (player.table)
	







		
		
		

