# Import
import random

# Functions
def start():
    print "Welcome to Tic-Tac-Toe!"
    print "The board will be displayed in the similar format of your numberpad"
    print "You are encouraged to refer to that"

def playAgain():
    print "Thanks for playing!"
    print "Play Again? (Y/N)"
    again = raw_input().upper()

    if again == 'Y':
        return True
    else:
        return False

def drawBoard(board):
    # Follows the numberpad keys
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def isWin(board, letter):
    # Check Win Conditions
    # 8 Win conditions
    # b - board, l - player letter
    return((board[7] == letter and board[8] == letter and board[9] == letter) or
           (board[4] == letter and board[5] == letter and board[6] == letter) or
           (board[1] == letter and board[2] == letter and board[3] == letter) or
           (board[7] == letter and board[5] == letter and board[3] == letter) or
           (board[7] == letter and board[4] == letter and board[1] == letter) or
           (board[8] == letter and board[5] == letter and board[2] == letter) or
           (board[9] == letter and board[6] == letter and board[3] == letter) or
           (board[9] == letter and board[5] == letter and board[1] == letter))

def holdBoard(board):
    # For System Checking
    boardCopy = []

    for i in board:
        boardCopy.append(i)
    return boardCopy

def isEmpty(board, move):
    return board[move] == ' '

def isPlayerMove(board):
    move = ' '
    arr = '1 2 3 4 5 6 7 8 9'.split()
    while move not in arr or not isEmpty(board, int(move)): 
        print "Your turn. (Select from 1 to 9)"
        move = raw_input()
        if isEmpty(board, int(move)) == False:
            print "Invalid move. It has been occupied"
    return int(move)

def setMove(board, move, letter):
    board[move] = letter

def isFull(board):
    for i in range(1, 10):
        if isEmpty(board, i):
            return False
    return True

# Computer's Turn
def aiTurn(board, aiLetter, playerLetter):
    """
    The "Perfect" Strategy
    1. Win: If player has 2 in a row, play 3rd to win
    2. Block: If oppo has 2 in a row, play 3rd to block
    3. Fork: Create opportunity where player has 2 threats to win
    4. Blocking Fork:
        1. Create two in a row to force the oppo into defending
            ie. if "X" has two oppo and "O" is center, "O" must not play corner
        2. If the oppo can fork, player should block the fork
    5. Center: Player marks center (as first move), but does not make difference for 
        equally perfect players
    6. Opposite corner: If oppo is in corner, play oppo corner
    7. Empty corner: Play in a corner square
    8. Empty side: Play in middle square on any of the 4 sides
    """
    for move in range(1, 10):
        hold = holdBoard(board)
        # Check if can win in next move
        if isEmpty(hold, move):
            setMove(hold, move, aiLetter) # Winning Turn
            if isWin(hold, aiLetter):
                return move

    for move in range(1, 10):
        hold = holdBoard(board)
        if isEmpty(hold, move):
            setMove(hold, move, playerLetter) # Blocking Turn
            if isWin(hold, playerLetter):
                return move
    
    # Check Center Empty
    if isEmpty(board, 5):
        return 5

    # If Center empty, take corner
    move = ranChoice(board, [1, 3, 7, 9])
    if move != None:
        return move

    # If center and corners are taken, no block or win
    return ranChoice(board, [2, 4, 6, 8])

# Choosing Random from list
def ranChoice(board, moves):
    possibleMoves = []
    for i in moves:
        if isEmpty(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Main
start()
while True:
    print "Do you wish to go first? (Y/N)"
    goFirst = raw_input().upper()
    # Player One plays X, player Two plays O
    if goFirst == 'Y':
        playerLetter = 'X'
        aiLetter = 'O'
        turn = 'player'
    else:
        aiLetter = 'X'
        playerLetter = 'O'
        turn = 'computer'
    board = [' '] * 10 #ignoring index 0
    drawBoard(board)

    isPlaying = True

    while isPlaying:
        if turn == 'player':
            # Player's turn
            move = isPlayerMove(board)
            setMove(board, move, playerLetter)
            drawBoard(board)

            if(isWin(board,playerLetter)):
                #Check if Win
                print "You won!"
                isPlaying = False

            else:
                if(isFull(board)):
                    #Check if Tie
                    print "It's a tie!"
                    isPlaying = False
                else:
                    #Handover turn
                    turn = 'computer'

        
        if turn == 'computer':
            # Compuer's turn

            move = aiTurn(board, aiLetter, playerLetter)
            setMove(board, move, aiLetter)
            drawBoard(board)

            if(isWin(board,aiLetter)):
                #Check if Win
                print "You lost!"
                isPlaying = False
            else:
                if(isFull(board)):
                    #Check if Tie
                    print "It's a tie!"
                    isPlaying = False
                else:
                    #Handover turn
                    turn = 'player'
    
    if not playAgain():
        break
