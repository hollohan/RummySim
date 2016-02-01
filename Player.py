from findTrips import findTrips
from findQuads import findQuads
from findRun import findRun
from addPoints import addPoints
from uniqNvalue import uniqNvalue
from random import shuffle

class Player:

	def __init__(self, id):
		self.hand = []
		self.table = []
		self.id = id
		
	def turn(self, board, deck):
		
		print ('\tstarting hand')
		print ('\t-------------')
		print ('\t' + str(self.hand))
		
		# pick up from the board?
		boardhand = board + self.hand
		matches = findTrips(boardhand) + findQuads(boardhand) + findRun(boardhand)
		matchesFound = 0
		if matches:
			for match in matches:
				for card in match:
					try:
						if board.index(card):	matchesFound = 1
					except:
						pass
		
	
		# if matches found then we should draw from board
		if matchesFound:
			chosenMatches = uniqNvalue(matches)
			bIndex = -1
			for match in chosenMatches:
				for card in match:
					try:
						ind = board.index(card)
						if bIndex == -1:
							bIndex = ind
						elif ind < bIndex:
							bIndex = ind
					except:
						pass
						
			print ('\tdrawing from the board')
			print ('\t----------------------')
			print ('\t' + str(board[bIndex]))
			
			
			for i in range(bIndex, len(board)):
				self.hand.append(board.pop(bIndex))
				
			'''
			self.hand = self.hand + board[bIndex:]
			board = board[:bIndex]
			'''
				
		# if not we should draw from deck
		else:
			# draw a card
			newCard = deck.pop()
			print ('\tdrawing from the deck')
			print ('\t----------------------')
			print ('\t' + str(newCard))
			self.hand.append(newCard)
			
			
		print ('\thand after draw/pickup')
		print ('\t----------------------')
		print ('\t' + str(self.hand))		
		
		
		# do i have any matches?
		matches = findTrips(self.hand) + findQuads(self.hand) + findRun(self.hand)
		if matches:
			print ('\tmatches found')
			print ('\t--------------------')
			print ('\t' + str(matches))
			
			chosenMatches = uniqNvalue(matches)
			
			print ('\tdropping matches')
			print ('\t---------------')
			print ('\t' + str(chosenMatches))
			for match in chosenMatches:
				self.table.append(match)
				for card in match:
						self.hand.pop(self.hand.index(card))
			print ('\thand after dropping points')
			print ('\t--------------------------')
			print ('\t' + str(self.hand))
		
		
		
		
		# -!- must also check table
		
		
		
		
		# discard one card randomly
		shuffle(self.hand)
		discard = self.hand.pop()
		print ('\tdiscarding')
		print ('\t----------')
		print ('\t' + str(discard))
		board.append(discard)
		
		print ('\tending hand')
		print ('\t-----------')
		print ('\t' + str(self.hand))
		
		
		
