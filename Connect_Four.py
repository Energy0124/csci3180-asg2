# CSCI3180 Principles of Programming Languages
#
# --- Declaration ---
#
# I declare that the assignment here submitted is original except for source
# material explicitly acknowledged. I also acknowledge that I am aware of
# University policy and regulations on honesty in academic work, and of the
# disciplinary guidelines and procedures applicable to breaches of such policy
# and regulations, as contained in the website
# http://www.cuhk.edu.hk/policy/academichonesty/
#
# Assignment 2
# Name : Ling Leong
# Student ID : 1155062557
# Email Addr : alanalan0124@yahoo.com.hk


import abc
import copy
import itertools
import random
import sys


class GameBoard:
    def __init__(self):
        self.board = [[' '] * 6 for _ in range(7)]
        self.column_top = [0] * 7

    def is_valid_move(self, column):
        column -= 1
        if not self.column_top[column] < 6:
            return False
        else:
            return True

    def is_full(self):
        full = True
        for top in self.column_top:
            if top < 5:
                full = False
                break
        return full

    # column must be between 1-7
    def play_on_column(self, column, symbol):
        column -= 1
        if not self.column_top[column] < 6:
            return False
        else:
            self.board[column][self.column_top[column]] = symbol
            self.column_top[column] += 1
            return True

    def is_won(self, player_symbol):
        connected_list = []
        # check vertical connect 4
        for column, column_list in enumerate(self.board):
            temp_list = []
            for row, symbol in enumerate(column_list):
                if symbol == player_symbol:
                    temp_list.append([column, row])
                else:
                    if len(temp_list) >= 4:
                        connected_list.append(temp_list)
                    temp_list = []
            if len(temp_list) >= 4:
                connected_list.append(temp_list)
        # check horizontal connect 4
        for row in range(6):
            temp_list = []
            for column in range(7):
                if self.board[column][row] == player_symbol:
                    temp_list.append([column, row])
                else:
                    if len(temp_list) >= 4:
                        connected_list.append(temp_list)
                    temp_list = []
            if len(temp_list) >= 4:
                connected_list.append(temp_list)
        # check diagonal connect 4 (\ direction)
        for sum_of_index in range(6 + 7 - 2):
            temp_list = []
            for row in range(6):
                for column in range(7):
                    if row + column == sum_of_index:
                        # print [column, row]
                        if self.board[column][row] == player_symbol:
                            temp_list.append([column, row])
                        else:
                            if len(temp_list) >= 4:
                                connected_list.append(temp_list)
                            temp_list = []
                if len(temp_list) >= 4:
                    connected_list.append(temp_list)
        # check diagonal connect 4 (/ direction)
        # temp_board = list(reversed(self.board))
        for sum_of_index in range(6 + 7 - 2):
            temp_list = []
            for row in range(6):
                for column in range(7):
                    if row + column == sum_of_index:
                        # print [6-column, row]
                        if self.board[6 - column][row] == player_symbol:
                            temp_list.append([6 - column, row])
                        else:
                            if len(temp_list) >= 4:
                                connected_list.append(temp_list)
                            temp_list = []
                if len(temp_list) >= 4:
                    connected_list.append(temp_list)

        connected_list.sort()
        return list(key for key, _ in itertools.groupby(connected_list))


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def highlight_text(text):
        return "\033[7m" + text + "\033[m"

    @staticmethod
    def opponent_symbol(symbol):
        if symbol == 'O':
            return 'X'
        else:
            return 'O'


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
                if not 0 < next_move < 8:
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
    def score(self, game_board, column):
        future_board = copy.deepcopy(game_board)
        if future_board.is_valid_move(column):
            future_board.play_on_column(column, self.player_symbol)
            if future_board.is_won(self.player_symbol):
                return 1000
            for counter_move in range(1, 8):
                future_board2 = copy.deepcopy(future_board)
                if future_board2.is_valid_move(counter_move):
                    future_board2.play_on_column(counter_move, Utils.opponent_symbol(self.player_symbol))
                    # print str(future_board2.is_won(Utils.opponent_symbol(self.player_symbol)))
                    if len(future_board2.is_won(Utils.opponent_symbol(self.player_symbol))) != 0:
                        return -1000
            return 0
        else:
            return -10000

    def next_column(self, game_board):
        if game_board.is_full():
            return False
        column_range = range(1, 8)
        score_list = []
        for column in column_range:
            score_list.append([self.score(game_board, column), column])
        score_list.sort()
        groups = []
        for key, group in itertools.groupby(score_list, lambda x: x[0]):
            score_group = []
            for pair in group:
                score_group.append(pair)
            # print str(pair) + " is " + str(key)
            # print
            groups.append(score_group)
        groups.sort(reverse=True)
        # print str(groups)
        # print random.choice(groups[0])[1]
        return random.choice(groups[0])[1]


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
        # won player
        self.won_player = self.player1
        # connected set
        self.connected_list = []
        self.highlight_board = [[False] * 6 for _ in range(7)]

    # - Start a new game and play until winning/losing or draw.
    def start_game(self):
        print "Initial game board"
        self.print_game_board()

        while not self.won:
            # get next move from player1
            print "Player " + self.current_player.player_symbol + " turn."
            next_column = self.current_player.next_column(self.game_board)
            if not next_column:
                print "no more valid placement, game ended"
                break
            successfully_placed = self.game_board.play_on_column(next_column, self.current_player.player_symbol)
            if not successfully_placed:
                print "invalid placement, aborting program"
                break
            else:
                print "Player " + self.current_player.player_symbol + " plays on column " + str(next_column)
            self.print_game_board()
            self.connected_list = self.game_board.is_won(self.current_player.player_symbol)
            if len(self.connected_list) > 0:
                self.won = True
                self.won_player = self.current_player
            # debug print all winning combination
            # print str(connected_list)
            self.next_turn()
        if self.won:
            print "Player " + self.won_player.player_symbol + " wins the game!"
        else:
            print "Game draw."
        self.print_game_board()

    def next_turn(self):
        self.turn_count += 1
        self.turn = self.turn_count % 2

    # - Print out the game board in the command line window.
    def print_game_board(self):
        if self.won:
            self.highlight_board = [[False] * 6 for _ in range(7)]
            for connected in self.connected_list:
                for pair in connected:
                    self.highlight_board[pair[0]][pair[1]] = True
        print "| 1 | 2 | 3 | 4 | 5 | 6 | 7 | "
        print "-" * 30
        for row in reversed(range(6)):
            sys.stdout.write("|")
            for column in range(7):
                if self.won and self.highlight_board[column][row]:
                    sys.stdout.write(Utils.highlight_text(" " + self.game_board.board[column][row] + " ") + "|")
                else:
                    sys.stdout.write(" " + self.game_board.board[column][row] + " " + "|")
            sys.stdout.write(" ")
            sys.stdout.flush()
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
                                              "3. CleverAI \n"
                                              "Your choice is: "))
            except ValueError:
                print "Input is not a number, please try again."
            else:
                if not 0 < player_type < 4:
                    print "Input must be either 1, 2 or 3, please try again."
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
                    elif player_type == 3:
                        if player_number_string == "first":
                            self.player1 = CleverAI('O')
                            print "Player O is CleverAI"
                        elif player_number_string == "second":
                            self.player2 = CleverAI('X')
                            print "Player X is CleverAI"
                    break

    def setup(self):
        self.setup_player("first")
        self.setup_player("second")

    @property
    def current_player(self):
        if self.turn == 0:
            return self.player1
        else:
            return self.player2


connect_four = ConnectFour()
connect_four.setup()
connect_four.start_game()
