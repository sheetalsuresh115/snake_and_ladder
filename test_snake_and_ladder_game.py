import random
import unittest
from snakeAndLadder.SnakeAndLadderGame import Game

class TestSnakeAndLadder(unittest.TestCase):
    def setUp(self):
        self.board_game = Game()
        self.board_game.ladders = Game.generate_moving_objects(self, ladders_or_snakes='ladders')
        self.board_game.snakes = Game.generate_moving_objects(self, ladders_or_snakes='snakes')

    def test_generate_moving_object_ladders(self):
        self.setUp()
        for key in self.board_game.ladders.keys():
            #For Ladders start point will be less than end point
            assert key < self.board_game.ladders[key]

    def test_generate_moving_object_snakes(self):
        self.setUp()
        for key in self.board_game.snakes.keys():
            # For Snakes start point will be greater than end point
            assert key > self.board_game.snakes[key]

    def test_roll_dice(self):
        count = random.randint(1,3)
        self.board_game.initialiseSimulationVariables(count)
        roll = [dice_roll for dice_roll in range(1, 7)]
        #The dice roll would be a number between 1 to 6
        assert self.board_game.roll_dice(count) in roll

    def test_snake_and_ladder(self):
        no_of_simulations = random.randint(1,3)
        self.board_game.snake_and_ladder(no_of_simulations)
        final_pos_in_all_simulations = [self.board_game.curr_position[simulation] for simulation in range(1,no_of_simulations+1)]
        assert len(set(final_pos_in_all_simulations)) == 1 and 100 in set(final_pos_in_all_simulations)

    def test_snake_and_ladder_with_configurable_snakes_ladders_simulation(self):
        no_of_simulations = random.randint(1, 3)
        ladder_pos = self.board_game.generate_moving_objects('ladders')
        snake_pos = self.board_game.generate_moving_objects('snakes')
        self.board_game.snake_and_ladder(no_of_simulations, ladder_pos, snake_pos)
        final_pos_in_all_simulations = [self.board_game.curr_position[simulation] for simulation in
                                        range(1, no_of_simulations + 1)]
        assert ladder_pos == self.board_game.ladders
        assert snake_pos == self.board_game.snakes
        assert len(set(final_pos_in_all_simulations)) == 1 and 100 in set(final_pos_in_all_simulations)

    def test_biased_snake_and_ladder_with_more_snakes(self):
        no_of_simulations = random.randint(1, 3)
        ladder_pos = self.board_game.generate_moving_objects('ladders')
        #This board will have atleast 14 snakes.
        snake_pos = self.board_game.generate_moving_objects('snakes',14,20)
        self.board_game.snake_and_ladder(no_of_simulations, ladder_pos, snake_pos)
        final_pos_in_all_simulations = [self.board_game.curr_position[simulation] for simulation in
                                        range(1, no_of_simulations + 1)]
        assert ladder_pos == self.board_game.ladders
        assert snake_pos == self.board_game.snakes
        assert len(set(final_pos_in_all_simulations)) == 1 and 100 in set(final_pos_in_all_simulations)