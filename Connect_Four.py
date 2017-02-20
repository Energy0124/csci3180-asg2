import abc
import random


class GameBoard:
    def __init__(self):
        self.board = [[' '] * 6 for _ in range(7)]
        self.column_count = [0] * 7


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def highlight_text(text):
        return "\033[30;47m" + text + "\033[m"


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
        column_range = range(1, 7)
        for index, column in enumerate(game_board.column_count, 1):
            if column >= 6:
                column_range.remove(index)
        return random.choice(column_range)


class CleverAI(Player):
    def next_column(self, game_board):
        pass


class ConnectFour:
    # - Initialize the Connect Four game.
    def __init__(self):
        # - This is a two-dimensional array representing the game board.
        self.game_board = GameBoard()
        # - This is a variable representing Player O.
        self.player1 = Human('O')
        # - This is a variable representing Player X.
        self.player2 = Computer('X')
        # - This is a variable indicating the player that should play in the current turn.
        # 0 for first player, 1 for second
        self.turn_count = 0
        # turn number
        self.turn = self.turn_count % 2
        # reach win condition or not
        self.won = False

    # - Start a new game and play until winning/losing or draw.
    def start_game(self):
        while not self.won:
            self.print_game_board()
            # get next move from player1
            next_column = self.get_current_player().next_column(self.game_board)

    # - Print out the game board in the command line window.
    def print_game_board(self):
        print "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | "
        print "-" * 30
        for row in range(6):
            print "|",
            for column in range(7):
                print self.game_board.board[column][row] + " |",
            print
            print "-" * 30

    def setup_player(self, player_number_string):
        while True:
            try:
                player_type = int(raw_input("Please choose the "
                                            + player_number_string
                                            + " player: \n"
                                              "1. Computer \n"
                                              "2. Human \n"
                                              "Your choice is: "))
            except ValueError:
                print "Input is not a number, please try again."
            else:
                if player_type != 1 and player_type != 2:
                    print "Input must be either 1 or 2, please try again."
                else:
                    if player_type == 1:
                        if player_number_string == "first":
                            self.player1 = Computer('O')
                            print "Player O is Computer"
                        elif player_number_string == "second":
                            self.player2 = Computer('X')
                            print "Player X is Computer"
                    elif player_type == 2:
                        if player_number_string == "first":
                            self.player1 = Human('O')
                            print "Player O is Human"
                        elif player_number_string == "second":
                            self.player2 = Human('O')
                            print "Player X is Human"
                    break

    def setup(self):
        self.setup_player("first")
        self.setup_player("second")

    def get_current_player(self):
        if self.turn == 0:
            return self.player1
        else:
            return self.player2


connect_four = ConnectFour()
connect_four.setup()
connect_four.start_game()
