"""
Tic Tac Toe
by Joseph
"""
#dictionary to hold the spaces
SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#string constants
X = 'X'
O = 'O'
BLANK = ' '

def main(): 
    print('2-player Tic-Tac-Toe (no AI)')
    gamePlace = makeBlankBoard()
    currentPlayer = O
    nextPlayer = X
    
    while True: 
        print(drawBoard(gamePlace))
        move = None
        while not verifySpace(gamePlace, move):
            print(f'It is {currentPlayer} turn. (1-9)')
            move = input('> ')
        updateBoard(gamePlace, move, currentPlayer)

        if determineWinner(gamePlace, currentPlayer):
            print(drawBoard(gamePlace))
            print(f'{currentPlayer} has won the game!')
            break
        elif isBoardFull(gamePlace):
            print(drawBoard(gamePlace))
            print('The game is a tie.')
            break
        #changes turns
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing')

def makeBlankBoard():
    """
    Create a new blank board to play
    """
    #Map of space numbers: 1|2|3
    #                      -+-+-
    #                      4|5|6
    #                      -+-+-
    #                      7|8|9
    board = {}

    for space in SPACES:
        board[space] = BLANK #makes board blank
    return board

def verifySpace(board, space):
    """
    Returns true if the space is blank and is a valid space number
    """
    return space in SPACES and board[space] == BLANK

def drawBoard(board):
    """
    Draws the board
    """
    return '''
      {}|{}|{}     1 2 3
      -+-+-
      {}|{}|{}     4 5 6
      -+-+-
      {}|{}|{}     7 8 9'''.format(board['1'], board['2'], board['3'],
                                   board['4'], board['5'], board['6'],
                                   board['7'], board['8'], board['9'])

def determineWinner(board, player):
    b, p = board, player
    #checking if there are three in the row
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['1'] == b['5'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p))

def isBoardFull(board):
    """Checks if board is full"""
    for space in SPACES:
        if board[space] == BLANK:
            return False
    return True

def updateBoard(board, space, mark):
    """Sets the space on the baord to mark"""
    board[space] = mark

if __name__ == '__main__':
    main()

            
            
