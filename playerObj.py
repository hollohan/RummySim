class Player:
	def __init__(self, id):	# init
		self.hand = [] # will store players hand
		self.table = []
		self.id = id	
		
	def turn(self, deck, board):
		print ('-'*25 + str(self.id) + '-'*25)
		#print (str(self))
		print ('--- starting hand ---')
		print (self.formatCard(self.hand))
			
		# check to see if we can make points from the board, if we can, draw from board
		loc = -1
		if len(board):	
			loc = self.pointsFromBoard(board)
			if loc > -1:
				board = board[:loc]
				#print ('--- the real new board ---')
				#print (self.formatCard(board))
		if loc == -1:
			#draw card from deck
			# check for cards left in deck
			try:
				player.hand.append(deck.pop())
			except:
				print ('--- unable to draw card from deck ---')
				return -1
			print ('--- hand after draw ---')
			print (self.formatCard(self.hand))

			
		
		# check if there's any points
		self.haveHand() # returns True with no point
		
		# discard a card (at random)
		random.shuffle(self.hand)
		# check for no discard
		try:
			discard = self.hand.pop()
		except:
			print ('--- unable to discard ---')
			return -1	
		print ('--- discard '),
		for val in discard:
			print (val),
		print ('---')
		board.append(discard)
		#print ('--- board ---')
		#print (self.formatCard(board))
		
		# print end hand
		print ('--- ending hand ---')
		print (self.formatCard(self.hand))
		print ('-'*51)
		print ('')
		return board
		
	def haveHand(self):	# check to see if we have a hand
		"""
		# check for 3 of a kind
		# sort hand by suit
		self.hand.sort()
		print ('--- hand sorted by value ---')
		print (self.formatCard(self.hand))
		
		i = 0
		while i < len(self.hand):
			#print ('\t\ti = ' + str(i))
			# break to avoid index out of bounds
			#print ('\t\tcomparing ' + str(i) + ' > ' + str(len(self.hand)-2))
			if i > len(self.hand) - 2:	
				#print('\t\t--- break ---')
				break
			
			for x in range(i, len(self.hand)-1):
				#print ('\t\t\tx = ' + str(x))
				#print ('\t\t\tcomparing ' + str(self.hand[x][0]) + ' AND ' + str(self.hand[x+1][0]))
				if self.hand[x][0] != self.hand[x+1][0]:
					#print ('\t\t\t--- X break --- these two did not match')
					break
			# the following fixes a bug that occurs when the highest 3 or four cards are all the same vaule
			#print ('\t\t\tcomparing x == len(self.hand)-1 AND pattern match -- ' + str(x) + ' == ' + str(len(self.hand)-2))
			if x == len(self.hand)-2 and self.hand[x][0] == self.hand[x+1][0]:
				#print ('\t\t\incrementing x, was ' + str(x)),
				x = x+1
				#print (' but is now ' + str(x))
			# x-i is length of pattern match, must be at least 3 to earn points, can be 3 or 4 here
			# i is starting point of  hand
			# if 2+(3 matches) then add hand to table
			#print ('\t--- length of match: ' + str(x-i))
			if x-i > 1:
				print ('\t--- points found in hand ---')
				holder = [] # used to make sure we add a list to the table
				for z in range(x-i+1):
						holder.append(self.hand.pop(i))
				print('\t--- adding points --- ' + self.formatCard(holder))
				self.table.append(holder)
				# i-1 must occur to reset the check on that position	
				#i = i-1 # this doesn't work due to iteration or something
				continue
			i = i+1
		"""
			
		# check for straight
		# sort hand by suit
		self.hand.sort()
		self.hand.sort(key=lambda x: x[1])
		print ('--- hand sorted by suit ---')
		print (self.formatCard(self.hand))
		
		i = 0
		while i < len(self.hand):
			#print ('\t\ti = ' + str(i))
			# break to avoid index out of bounds
			#print ('\t\tcomparing ' + str(i) + ' > ' + str(len(self.hand)-2))
			if i > len(self.hand) - 2:	
				#print('\t\t--- break ---')
				break
			
			for x in range(i, len(self.hand)-1):
				#print ('\t\t\tx = ' + str(x))
				if self.hand[x][1] != self.hand[x+1][1] or self.hand[x][0] + 1 != self.hand[x+1][0]:
					#print ('\t\t\t--- X break --- these two did not match')
					break
			# the following fixes a bug that occurs when the highest 3 or four cards are all the same vaule
			#print ('\t\t\tcomparing x == len(self.hand)-1 AND pattern match -- ' + str(x) + ' == ' + str(len(self.hand)-2))
			if x == len(self.hand)-2 and self.hand[x][0] == self.hand[x+1][0]:
				#print ('\t\t\incrementing x, was ' + str(x)),
				x = x+1
				#print (' but is now ' + str(x))
			# x-i is length of pattern match, must be at least 3 to earn points, can be 3 or 4 here
			# i is starting point of  hand
			# if 2+(3 matches) then add hand to table
			#print ('\t--- length of match: ' + str(x-i))
			if x-i > 1:
				print ('\t--- points found in hand ---')
				holder = [] # used to make sure we add a list to the table
				for z in range(x-i+1):
						holder.append(self.hand.pop(i))
				print('\t--- adding points --- ' + self.formatCard(holder))
				self.table.append(holder)
				# i-1 must occur to reset the check on that position	
				#i = i-1 # this doesn't work due to iteration or something
				continue
			i = i+1
		""" the old way
		# check for straight
		for i in range(len(self.hand)):
			# break
			if i > len(self.hand) - 3:	break
			
			# if three cards of same suit && incremental
			if self.hand[i][1]*2 == self.hand[i+1][1] + self.hand[i+2][1]:
				if self.hand[i+2][0] - self.hand[i+1][0] == 1:
					if self.hand[i+1][0] - self.hand[i][0] == 1:
						# we have a straight
						self.table.append([self.hand.pop(i), self.hand.pop(i), self.hand.pop(i)])
						print ('--- points added ---')
						print (self.formatTable(self.table))
		"""
		return False

	def pointsFromBoard(self, board):
		#print ('---- checking board ----')
		import copy
		# copy board
		boardCopy = copy.deepcopy(board)
		# add hand to board copy
		boardCopy = boardCopy + self.hand
		# sort
		boardCopy.sort()
		"""
		# check for 3 or more of a kind
		i = 0
		while i < len(boardCopy):
			# break to avoid index out of bounds
			if i > len(boardCopy) - 2:	
				break
			
			for x in range(i, len(boardCopy)-1):
				if boardCopy[x][0] != boardCopy[x+1][0]:
					break
			# the following fixes a bug that occurs when the highest 3 or four cards are all the same vaule
			if x == len(boardCopy)-2 and boardCopy[x][0] == boardCopy[x+1][0]:
				x = x+1
			# x-i is length of pattern match
			# i is starting point of  hand which will need to be returned
			# if 2+(3 matches) then return starting point / draw/add cards to hand
			if x-i > 1:
				# find out which card is deepest in the board and find location
				loc = -1
				for x in range(x-i):
					if boardCopy[i+x] in board and loc == -1:
						loc = board.index(boardCopy[i+x])
					elif boardCopy[i+x] in board:
						if board.index(boardCopy[i+x]) < loc:
							loc = board.index(boardCopy[i+x])
						
				print ('--- drawing from board starting at '),
				print (self.formatCard(board[loc:loc+1])),
				print ('-X of a kind-')
				
				# pickup cards / add cards to hand
				self.hand = self.hand + board[loc:]
				# remove cards from board
				board = board[:loc] #this is not nec. as it doesn't work and we alter it in the next func anyway
				return loc
			i = i+1
		"""
		# copy board
		boardCopy = copy.deepcopy(board)
		# add hand to board copy
		boardCopy = boardCopy + self.hand
		# sort
		boardCopy.sort()
		boardCopy.sort(key=lambda x: x[1])
		#print ('\t\t\t- board+hand - ' + self.formatCard(boardCopy))
		i = 0
		while i < len(boardCopy):
			#print ('\t\ti = ' + str(i))
			# break to avoid index out of bounds
			#print ('\t\tcomparing ' + str(i) + ' > ' + str(len(self.hand)-2))
			if i > len(boardCopy) - 2:	
				#print('\t\t--- break ---')
				break
			
			for x in range(i, len(boardCopy)-1):
				#print ('\t\t\tx = ' + str(x))
				if boardCopy[x][1] != boardCopy[x+1][1] or boardCopy[x][0] + 1 != boardCopy[x+1][0]:
					#print ('\t\t\t--- X break --- these two did not match')
					break
			# the following fixes a bug that occurs when the highest 3 or four cards are all the same vaule
			#print ('\t\t\tcomparing x == len(self.hand)-1 AND pattern match -- ' + str(x) + ' == ' + str(len(self.hand)-2))
			if x == len(boardCopy)-2 and boardCopy[x][0] == boardCopy[x+1][0]:
				#print ('\t\t\incrementing x, was ' + str(x)),
				x = x+1
				#print (' but is now ' + str(x))
			# x-i is length of pattern match, must be at least 3 to earn points, can be 3 or 4 here
			# i is starting point of  hand
			# if 2+(3 matches) then add hand to table
			#print ('\t--- length of match: ' + str(x-i))
			if x-i > 1:
				# find out which one is deepest in the board and find location
				loc = -1
				for z in range(x-i):
					if boardCopy[i+z] in board and loc == -1:
						loc = board.index(boardCopy[i+z])
					elif bo
					
					ardCopy[i+z] in board:
						if board.index(boardCopy[i+z]) < loc:
							loc = board.index(boardCopy[i+z])			
				# update user	
				#print ('\t--- found the straight ---')
				print ('\t\t\t--- loc: ' + str(loc))
				print ('--- drawing from board starting at '),
				print (self.formatCard(board[loc:loc+1])),
				print ('-S-')
			
				# pickup cards
				# add cards to hand
				self.hand = self.hand + board[loc:]
				# remove cards from board
				board = board[:loc]
				print ('--- New Hand ---')
				print ('\t' + self.formatCard(self.hand))
				return loc
			i = i+1
		""" the old way
		# check for straight
		for i in range(len(boardCopy)):
			# break
			if i > len(boardCopy) - 3:	break
			
			# if three cards of same suit && incremental
			
			if boardCopy[i][1]*2 == boardCopy[i+1][1] + boardCopy[i+2][1]:
				if boardCopy[i+2][0] - boardCopy[i+1][0] == 1:
					if boardCopy[i+1][0] - boardCopy[i][0] == 1:
						# we have a straight
						# find out which one is deepest in the board and find location
						loc = -1
						for x in range(3):
							if boardCopy[i+x] in board and loc == -1:
								loc = board.index(boardCopy[i+x])
							elif boardCopy[i+x] in board:
								if board.index(boardCopy[i+x]) < loc:
									loc = board.index(boardCopy[i+x])
						
						# update user	
						#print ('\t--- found the straight ---')
						print ('--- drawing from board starting at '),
						print (self.formatCard(board[loc:loc+1])),
						print ('-S-')
						
						# pickup cards
						# add cards to hand
						self.hand = self.hand + board[loc:]
						# remove cards from board
						board = board[:loc]
						print ('--- New Hand ---')
						print ('\t' + self.formatCard(self.hand))
						return loc
		"""
		return -1
		
	def formatCard(self,hand):
	
		outString = ''
	
		for card in hand:
			for val in card:
				try:
					outString = outString + str(val)
				except:
					outString = outString + val
			outString = outString + ', '
	
	
		return outString	
		
	def formatTable(self, table):
		#outString = ''
		#print (table)
		for points in table:
			print (self.formatCard(points))	# cannot seem to append this to outstring but this works
			# ouString = outString + '\n' + self.formatCard(points)
		#return outString
		
		
		
def summary(players):		
	# print ea players table
	print ('------- Score --------')
	print ('----------------------')
	for player in players:
		print('---' + str(player.id) + '---')
		print (player.formatTable(player.table))
	exit()

# deal 7 cards to player

# pick a card at random

# create deck/board
deck = []
board = []
suits = ['h', 'd', 's', 'c']
for suit in suits:
	[deck.append([z, suit]) for z in range(13)]
# print (deck)
# print ("--- " + str(len(deck)) + " cards in the deck ---")


# shuffle the deck
import random
random.shuffle(deck)
# print (deck)

# create players
x=4		# number of players
players = []
for i in range(x):
	newPlayer = Player(i)
	players.append(newPlayer)
# print(players)

# deal 7 cards to each player
for i in range(7):
	for player in players:
		player.hand.append(deck.pop())
		
# print all players cards
for player in players:
	print ('------ player ------ ' + str(player.id))
	print(player.formatCard(player.hand))
	print('-'*20)

print ('\n\n')

# run players through range(x) turns
for i in range(7):
	for player in players:
		print ('--- turn ' + str(i) + ' ---')
		print ('--- board ' + player.formatCard(board))
		print ('')
		board = player.turn(deck, board)
		if board == -1:
			summary(players)
			
summary(players)
		
	
