
# Create array of possible moves
possibleMoves = []

# Attain all the empty positions
availableSpace = emptyIndex(board)

# Take turns doing minmax
alpha = -999
beta = 999

def minmax(depth, player, alpha, beta):
    if(len(availableSpace) == 0):
        # Once every movement has been placed, evaluate if its best
        score = evaluate()
        return score

    # Children = availableSpace

    for i in availableSpace:
        # AI Turn | Maximise | Alpha
        if(player == computer):
            score = minmax(board, user, alpha, beta) 
            if(score > alpha):
                alpha = score
                bestSpace = i

            
        else: # User Turn | Minimise | Beta
            score = minmax(board, computer, alpha, beta)
            if(score < beta):
                beta = score
                bestSpace = i
        
        # Undo Move
        board[i] = ' '
        if(alpha >= beta):
            break
    
    return alpha if (player == computer) else beta


