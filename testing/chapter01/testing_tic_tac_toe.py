import unittest
import numpy as np
import numpy.testing as nptest
from chapter01 import tic_tac_toe as ttt
from chapter01.tic_tac_toe import TicTacToeGenerator as tttgen, TicTacToeUtils as tttutils


class TestTicTacToe(unittest.TestCase):

    def assert_coordinate_bounds(self, coordinates):
        x, y = coordinates
        self.assertTrue(0 <= x <= 2)
        self.assertTrue(0 <= y <= 2)

    def test_index_to_board_coordinates(self):

        for i in range(0,9):
            coords = tttutils.index_to_board_coordinates(i)
            self.assert_coordinate_bounds(coords)

    def test_index_to_board_coordinates_oob_lower(self):
        self.assertRaises(IndexError, tttutils.index_to_board_coordinates, -1)

    def test_index_to_board_coordinates_oob_upper(self):
        self.assertRaises(IndexError, tttutils.index_to_board_coordinates, 9)

    def test_string_to_state(self):
        string = '---------'
        expected = ttt.EMPTY_BOARD
        state = tttutils.string_to_state(string)
        nptest.assert_array_equal(expected, state)

    def test_string_to_state_error(self):
        string = '-'
        self.assertRaises(ValueError, tttutils.string_to_state, string)

    def test_string_to_state_char(self):
        string = 'WONT WORK!'
        self.assertRaises(ValueError, tttutils.string_to_state, string)

    def test_is_winning_state_for_player(self):
        X = ttt.X
        EMPTY = ttt.EMPTY

        state = [X, X, X, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, EMPTY, EMPTY, X, X, X, EMPTY, EMPTY, EMPTY]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, X, X, X]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [X, EMPTY, EMPTY, X, EMPTY, EMPTY, X, EMPTY, EMPTY]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, X, EMPTY, EMPTY, X, EMPTY, EMPTY, X, EMPTY]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, EMPTY, X, EMPTY, EMPTY, X, EMPTY, EMPTY, X]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [X, EMPTY, EMPTY, EMPTY, X, EMPTY, EMPTY, EMPTY, X]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, EMPTY, X, EMPTY, X, EMPTY, X, EMPTY, EMPTY]
        self.assertTrue(tttutils.is_winning_state_for_player(state, X))

    def test_is_winning_state_for_player_false(self):
        X = ttt.X
        EMPTY = ttt.EMPTY
        O = ttt.O

        state = [X, X, O, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        self.assertFalse(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, EMPTY, EMPTY, EMPTY, X, X, EMPTY, EMPTY, EMPTY]
        self.assertFalse(tttutils.is_winning_state_for_player(state, X))

        state = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        self.assertFalse(tttutils.is_winning_state_for_player(state, X))


class TestRLTicTacToe(unittest.TestCase):

    def setUp(self):
        self.ai = ttt.RLTicTacToe(ttt.X)

    def test_move_exception(self):
        X = ttt.X
        O = ttt.O
        full_board = np.array([[X, O, X], [O, X, O], [X, O, X]])
        self.assertRaises(EnvironmentError, self.ai.move, full_board)

    def test_move_greedy(self):
        greedy_ai = ttt.RLTicTacToe(ttt.X, greedy_factor=1)
        X = ttt.X
        O = ttt.O
        EMPTY = ttt.EMPTY

        board = np.array([[X, EMPTY, X], [O, X, O], [O, EMPTY, EMPTY]])
        x, y = greedy_ai.move(board)
        self.assertTrue(0 <= x <= 2)
        self.assertTrue(0 <= y <= 2)

    def test_move_exploratory(self):
        exploratory_ai = ttt.RLTicTacToe(ttt.X, greedy_factor=0)

        empty_board = ttt.EMPTY_BOARD
        x, y = exploratory_ai.move(empty_board)
        self.assertTrue(0 <= x <= 2)
        self.assertTrue(0 <= y <= 2)








