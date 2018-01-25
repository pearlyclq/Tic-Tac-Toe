
value = 0
score = 0
alpha = -999
beta = 999
# alpha pruning
if(value > alpha):
	alpha = value

#beta pruning
if(value < beta):
	beta = value

hold = holdBoard(board)

#Scoring
if (isWin(hold, aiLetter)):
	score +=10
if (isFull(hold)):
	score += 0
if (isWin(hold, playerLetter)):
	score -=10

def checkNextTurnWin(board, letter):
	# retrieve an array of all available space
	# return the index of empty space into arrat
	# availSpace = array[]
	# if isEmpty(), availspace[].append(i)
	# test if each space is empty, will the winning condition be met
	# keep an array of winning condition possible location