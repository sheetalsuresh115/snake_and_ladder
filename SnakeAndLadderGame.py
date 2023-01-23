import random
from snakeAndLadder.GameStatistics import GameStatistics

class Game:
    def __init__(self):
        self.curr_position = {}
        self.ladders = {}
        self.snakes = {}
        self.simulation_count = 0
        self.game_statistics_obj = GameStatistics()
        self.list_of_six = []
        self.biggest_six_turn = []

    def generate_moving_objects(self,ladders_or_snakes,start =6 ,end=8):
        ''''This function generates ladders and snakes.'''
        moving_objects = {}

        #Assuming there would be 5 to 8 snakes and ladders in a game.
        for num in range(1,random.randint(start,end)):
            start_pos = random.randint(1, 97)
            end_pos = random.randint(start_pos+1, 99)
            if ladders_or_snakes == 'ladders':
                moving_objects[start_pos] = end_pos
            else:
                moving_objects[end_pos] = start_pos

        return moving_objects

    def roll_dice(self, count):
        """"This function is responsible for the logic of what happens after rolling the dice.
            Also considers climbing up a ladder and being swallowed by a snake.
        """

        print('Rolling Dice..')
        dice_rolled = random.randint(1, 6)
        print('Dice Rolled : ',dice_rolled)

        self.game_statistics_obj.set_stats_rolls_to_win_and_lucky_rolls(count, dice_rolled, curr_position = self.curr_position[count])

        if dice_rolled + self.curr_position[count] == 100:
            self.curr_position[count] += dice_rolled
            print('Game Over !!')
            return dice_rolled

        if dice_rolled + self.curr_position[count] > 100:
            #Nothing to be done, player would remain in the same position
            print('Need exact number to Finish the game : ', (100-self.curr_position[count]))
            return dice_rolled
        else:
            self.curr_position[count] += dice_rolled
            print('Moved to position : ',self.curr_position[count])

        if self.curr_position[count] in self.ladders:
            self.game_statistics_obj.set_stats_for_climb(count,curr_position = self.curr_position[count],\
                                                         ladder_end = self.ladders[self.curr_position[count]])

            self.curr_position[count] = self.ladders[self.curr_position[count]]
            print('Çlimbing up the Ladder to position : ',self.curr_position[count])

        elif self.curr_position[count] in self.snakes:
            self.game_statistics_obj.set_stats_for_descends(count,curr_position=self.curr_position[count],\
                                                            snake_end =self.snakes[self.curr_position[count]])

            self.curr_position[count] = self.snakes[self.curr_position[count]]
            print('Swallowed by a Snake to position : ', self.curr_position[count])

        self.game_statistics_obj.set_stats_for_lucky_rolls(count,self.snakes.keys(),\
                                                           curr_position =self.curr_position[count])

        return dice_rolled

    def initialiseSimulationVariables(self,count):
        ''''This function is responsible for initialising all the variables used inside a simulation.'''

        self.curr_position[count] = 0
        self.list_of_six =[]
        self.biggest_six_turn = []
        self.game_statistics_obj.rolls_to_win[count] = 0
        self.game_statistics_obj.no_of_climbs[count] = 0
        self.game_statistics_obj.no_of_slides[count] = 0
        self.game_statistics_obj.biggest_climb[count] = 0
        self.game_statistics_obj.biggest_slide[count] = 0
        self.game_statistics_obj.unlucky_rolls[count] = 0
        self.game_statistics_obj.lucky_rolls[count] = 0

    def snake_and_ladder(self, no_of_simulations=None,ladder_pos=None,snake_pos=None):
        ''''
            This function is responsible for Starting the game, initializing simulation variables,
            and rolling the dice.
        '''

        print('Welcome to the Snake and Ladder Game')
        print('This is a single player game.')
        try:
            if no_of_simulations:
                self.simulation_count = no_of_simulations
            else:
                self.simulation_count = random.randint(1,3)

            if ladder_pos:
                self.ladders = ladder_pos
            else:
                self.ladders = self.generate_moving_objects('ladders')

            if snake_pos:
                self.snakes = snake_pos
            else:
                self.snakes = self.generate_moving_objects('snakes')

            print('Ladders are located at : ',self.ladders)
            print('Snakes are located at : ',self.snakes)
            for count in range(1, self.simulation_count+1):
                print('\n###Simulation No: %d Begins' %count)
                self.initialiseSimulationVariables(count)

                while self.curr_position[count] != 100:
                    #Roll dice
                    dice_rolled = self.roll_dice(count)
                    if dice_rolled == 6:
                        self.list_of_six.append(dice_rolled)


                    while dice_rolled == 6 and self.curr_position[count] != 100:
                        #Keep rolling if you get 6
                        dice_rolled = self.roll_dice(count)
                        self.list_of_six.append(dice_rolled)

                    if self.list_of_six :
                        self.biggest_six_turn.append(self.list_of_six.copy())
                        self.list_of_six.clear()

                if self.biggest_six_turn:
                    self.game_statistics_obj.set_stats_longest_turn(self.biggest_six_turn,count)
                print('###End of Simulation :',count)

        except Exception as ex:
            print('Exception : ',ex)


if __name__ == "__main__":
    try:
        gameObj = Game()
        gameObj.snake_and_ladder(no_of_simulations = 3)
        #gameObj.snake_and_ladder(no_of_simulations=3,ladder_pos={6:10,45:78,80:86},snake_pos={88:80,60:35,54:40})
        gameObj.game_statistics_obj.get_min_avg_max_of_rolls_to_win()
        gameObj.game_statistics_obj.get_min_avg_max_of_no_of_climbs()
        gameObj.game_statistics_obj.get_min_avg_max_of_no_of_slides()
        gameObj.game_statistics_obj.get_biggest_climb()
        gameObj.game_statistics_obj.get_biggest_slide()
        gameObj.game_statistics_obj.get_longest_turn()
        gameObj.game_statistics_obj.get_unlucky_rolls()
        gameObj.game_statistics_obj.get_lucky_rolls()
    except Exception as ex:
        print('Exception : ', ex)

