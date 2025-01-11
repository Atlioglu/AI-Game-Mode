import unittest
from unittest.mock import MagicMock
from Algorithms import Algorithms
from GameActions import GameActions


class UnitTest(unittest.TestCase):
    def setUp(self):
        mock_actions = MagicMock()
        self.algorithms = Algorithms(mock_actions)

        default_board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
        ]
        self.game_actions = GameActions(default_board)

    def test_count_numbers_empty_board(self):
        board = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
        ]
        result = self.game_actions.count_numbers("black", board)
        self.assertEqual(result, 0)

    def test_count_numbers_filled_board(self):
        board = [
            ["black", "black", "white", "white", "", "", "", ""],
            ["black", "black", "white", "white", "", "", "", ""],
            ["", "", "", "", "black", "black", "", ""],
            ["", "", "", "", "black", "black", "", ""],
            ["white", "white", "white", "white", "black", "black", "", ""],
            ["white", "white", "white", "white", "black", "black", "", ""],
            ["", "", "", "", "black", "black", "", ""],
            ["", "", "", "", "black", "black", "", ""],
        ]
        result = self.game_actions.count_numbers("black", board)
        self.assertEqual(result, 16)  # Updated to match the correct count

    def test_count_numbers_mixed_board(self):
        board = [
            ["black", "white", "", "", "", "", "", ""],
            ["", "black", "white", "", "", "", "", ""],
            ["", "", "black", "white", "", "", "", ""],
            ["", "", "", "black", "white", "", "", ""],
            ["", "", "", "", "black", "white", "", ""],
            ["", "", "", "", "", "black", "white", ""],
            ["", "", "", "", "", "", "black", "white"],
            ["", "", "", "", "", "", "", "black"],
        ]
        result_black = self.game_actions.count_numbers("black", board)
        result_white = self.game_actions.count_numbers("white", board)
        self.assertEqual(result_black, 8)
        self.assertEqual(result_white, 7)

    def test_count_numbers_no_matches(self):
        board = [
            ["white", "white", "white", "white", "", "", "", ""],
            ["white", "white", "white", "white", "", "", "", ""],
            ["", "", "", "", "white", "white", "", ""],
            ["", "", "", "", "white", "white", "", ""],
            ["", "", "", "", "white", "white", "", ""],
            ["", "", "", "", "white", "white", "", ""],
            ["", "", "", "", "white", "white", "", ""],
            ["", "", "", "", "white", "white", "", ""],
        ]
        result = self.game_actions.count_numbers("black", board)
        self.assertEqual(result, 0)

    def test_select_greedy(self):
        self.algorithms.actions.future_moves.return_value = {
            (3, 2): {'number_of_cells': 5},
            (4, 5): {'number_of_cells': 3},
            (2, 1): {'number_of_cells': 7},
        }

        result = self.algorithms.select_greedy("black")

        self.assertEqual(result, (2, 1))  
        self.algorithms.actions.future_moves.assert_called_with("black")


if __name__ == "__main__":
    unittest.main()
