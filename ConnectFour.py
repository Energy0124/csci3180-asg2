import abc


class ConnectFour:
    # - Initialize the Connect Four game.
    def __init__(self):
        self.gameBoard = [[' '] * 6 for _ in range(7)]
        # - This is a two-dimensional array representing the game board.
        self.player1 = Human('O')
        # - This is a variable representing Player O.
        self.player2 = Computer('X')
        # - This is a variable representing Player X.
        self.turn = self.player1
        # - This is a variable indicating the player that should play in the current turn.

    # - Start a new game and play until winning/losing or draw.
    def start_game(self):
        pass

    # - Print out the game board in the command line window.
    def print_game_board(self):
        pass


class Player:
    __metaclass__ = abc.ABCMeta

    def __init__(self, player_symbol):
        self.playerSymbol = player_symbol

    @abc.abstractmethod
    def next_column(self, game_board):
        pass


class Human(Player):
    def next_column(self, game_board):
        pass



class Computer(Player):
    def next_column(self, game_board):
        pass
