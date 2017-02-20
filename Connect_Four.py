import abc
import random


class GameBoard:
    def __init__(self):
        self.board = [[' '] * 6 for _ in range(7)]
        self.column_top = [0] * 7

    def is_full(self):
        full = True
        for top in self.column_top:
            if top < 5:
                full = False
                break
        return full

    def play_on_column(self, column, symbol):
        column -= 1
        if not self.column_top[column] < 6:
            return False
        else:
            self.board[column][self.column_top[column]] = symbol
            self.column_top[column] += 1
            return True


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def highlight_text(text):
        return "\033[30;47m" + text + "\033[m"


class Player:
    __metaclass__ = abc.ABCMeta

    def __init__(self, player_symbol):
        self.player_symbol = player_symbol

    # return the next column to play as an int from 1 - 7, return False is there is not valid move
    @abc.abstractmethod
    def next_column(self, game_board):
        pass


class Human(Player):
    def next_column(self, game_board):
        while True:
            try:
                next_move = int(
                    raw_input("Which column do you want to play next? (1-7) \n"
                              "Your choice is: "))
            except ValueError:
                print "Input is not a number, please try again."
            else:
                if 1 > next_move > 7:
                    print "Your next move must be between 1 to 7, please try again."
                elif game_board.column_top[next_move - 1] >= 6:
                    print "Invalid move. Column " + str(next_move) + " is already full. Please try again."
                elif game_board.is_full():
                    return False
                else:
                    return next_move


class Computer(Player):
    def next_column(self, game_board):
        column_range = range(1, 8)
        for index, column_top in enumerate(game_board.column_top, 1):
            if column_top >= 6:
                column_range.remove(index)
        if len(column_range) == 0:
            return False
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
        print "Initial game board"
        self.print_game_board()

        while not self.won:
            # get next move from player1
            print "Player " + self.get_current_player().player_symbol + " turn."
            next_column = self.get_current_player().next_column(self.game_board)
            if not next_column:
                print "no more valid placement, game ended"
                break
            successfully_placed = self.game_board.play_on_column(next_column, self.get_current_player().player_symbol)
            if not successfully_placed:
                print "invalid placement, aborting program"
                break
            else:
                print "Player " + self.get_current_player().player_symbol + " plays on column " + str(next_column)
            self.print_game_board()
            self.next_turn()

    def next_turn(self):
        self.turn_count += 1
        self.turn = self.turn_count % 2

    # - Print out the game board in the command line window.
    def print_game_board(self):
        print "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | "
        print "-" * 30
        for row in reversed(range(6)):
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
                            self.player2 = Human('X')
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
