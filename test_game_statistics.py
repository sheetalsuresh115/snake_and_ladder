import unittest
from snakeAndLadder.SnakeAndLadderGame import Game
from snakeAndLadder.GameStatistics import GameStatistics
import random

class TestGameStatistics(unittest.TestCase):
    def setUp(self):
        self.board_game = Game()
        self.no_of_simulations = random.randint(1, 3)

    def test_get_min_avg_max_of_rolls_to_win(self):
        assert self.board_game.game_statistics_obj.rolls_to_win == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_min_avg_max_of_rolls_to_win()
        assert self.board_game.game_statistics_obj.rolls_to_win

    def test_get_min_avg_max_of_no_of_climbs(self):
        assert self.board_game.game_statistics_obj.no_of_climbs == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_min_avg_max_of_no_of_climbs()
        assert self.board_game.game_statistics_obj.no_of_climbs

    def test_get_min_avg_max_of_no_of_slides(self):
        assert self.board_game.game_statistics_obj.no_of_slides == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_min_avg_max_of_no_of_slides()
        assert self.board_game.game_statistics_obj.no_of_slides

    def test_get_biggest_climb(self):
        assert self.board_game.game_statistics_obj.biggest_climb == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_biggest_climb()
        assert self.board_game.game_statistics_obj.biggest_climb

    def test_get_biggest_slide(self):
        assert self.board_game.game_statistics_obj.biggest_slide == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_biggest_slide()
        assert self.board_game.game_statistics_obj.biggest_slide

    def test_get_unlucky_rolls(self):
        assert self.board_game.game_statistics_obj.unlucky_rolls == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_unlucky_rolls()
        assert self.board_game.game_statistics_obj.unlucky_rolls

    def test_get_lucky_rolls(self):
        assert self.board_game.game_statistics_obj.lucky_rolls == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_lucky_rolls()
        assert self.board_game.game_statistics_obj.lucky_rolls

    def test_get_longest_turn(self):
        assert self.board_game.game_statistics_obj.biggest_turn == {}
        self.board_game.snake_and_ladder(self.no_of_simulations)
        self.board_game.game_statistics_obj.get_longest_turn()
        assert self.board_game.game_statistics_obj.biggest_turn

    def test_set_stats_longest_turn(self):
        count = self.no_of_simulations
        biggest_six_turn = [[6,6,6],[6,6,6,1],[6,4],[6,6,6,6,10],[6,6,6,6,2]]
        self.board_game.game_statistics_obj.set_stats_longest_turn(biggest_six_turn, count)

        assert self.board_game.game_statistics_obj.biggest_turn[count] == [[6,6,6,6,10],[6,6,6,6,2]]
