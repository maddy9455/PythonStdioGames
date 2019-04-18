# An object-oriented Tic Tac Toe game.
# By Al Sweigart al@inventwithpython.com

# Setting up constants:
ALL_SPACES = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
X, O, BLANK = 'X', 'O', ' '

def main():
    """Runs a game of Tic Tac Toe."""
    print('Welcome to Tic Tac Toe!')
    gameBoard = TicTacToeBoard()
    turn, nextTurn = X, O

    while True:
        gameBoard.drawBoard()
        move = gameBoard.getPlayerMove(turn)
        gameBoard.setSpace(move, turn)

        if gameBoard.isWinner(turn):
            gameBoard.drawBoard()
            print(turn + ' has won the game!')
            break
        elif gameBoard.isBoardFull():
            gameBoard.draw()
            print('The game is a tie!')
            break

        turn, nextTurn = nextTurn, turn

class TicTacToeBoard:
    def __init__(self):
        """Create a new, blank tic tac toe board."""
        self.spaces = {}
        for space in ALL_SPACES:
            self.spaces[space] = BLANK

    def drawBoard(self):
        """Display a text-representation of the board."""
        print(f'''
          {self.spaces['7']}|{self.spaces['8']}|{self.spaces['9']}  7 8 9
          -+-+-
          {self.spaces['4']}|{self.spaces['5']}|{self.spaces['6']}  4 5 6
          -+-+-
          {self.spaces['1']}|{self.spaces['2']}|{self.spaces['3']}  1 2 3''')

    def isWinner(self, player):
        """Return True if player is a winner on this TicTacToeBoard."""
        bo, p = self.spaces, player # Shorter names for "syntactic sugar".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((bo['7'] == p and bo['8'] == p and bo['9'] == p) or
                (bo['4'] == p and bo['5'] == p and bo['6'] == p) or
                (bo['1'] == p and bo['2'] == p and bo['3'] == p) or
                (bo['7'] == p and bo['4'] == p and bo['1'] == p) or
                (bo['8'] == p and bo['5'] == p and bo['2'] == p) or
                (bo['9'] == p and bo['6'] == p and bo['3'] == p) or
                (bo['7'] == p and bo['5'] == p and bo['3'] == p) or
                (bo['9'] == p and bo['5'] == p and bo['1'] == p))

    def getPlayerMove(self, player):
        """Let the player type in their move."""
        space = None
        while space not in ALL_SPACES or not self.spaces[space] == BLANK:
            print(f'What is {player}\'s move? (1-9)')
            space = input().upper()
        return space

    def isBoardFull(self):
        """Return True if every space on the board has been taken."""
        for space in ALL_SPACES:
            if self.spaces[space] == BLANK:
                return False
        return True

    def setSpace(self, space, player):
        """Sets the space on the board to player."""
        self.spaces[space] = player

if __name__ == '__main__':
    main() # Call main() if this module is run, but not when imported.
