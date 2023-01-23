class GameStatistics:
    def __init__(self):
        self.rolls_to_win = {}
        self.no_of_climbs = {}
        self.no_of_slides = {}
        self.biggest_climb = {}
        self.biggest_slide = {}
        self.unlucky_rolls = {}
        self.lucky_rolls = {}
        self.biggest_turn = {}

    def get_min_avg_max_of_rolls_to_win(self):
        print('Rolls')
        print('Minimum no:of rolls to Win : ',min(self.rolls_to_win.values()))
        total = len(self.rolls_to_win.values())
        print('Average no:of rolls to Win : ',round(sum(self.rolls_to_win.values())/total,2))
        print('Maximum no:of rolls to Win : ', max(self.rolls_to_win.values()))

    def get_min_avg_max_of_no_of_climbs(self):
        print('Climbs')
        print('Minimum no:of climbs : ', min(self.no_of_climbs.values()))
        total = len(self.no_of_climbs.values())
        print('Average no:of climbs : ', round(sum(self.no_of_climbs.values())/total,2))
        print('Maximum no:of climbs : ', max(self.no_of_climbs.values()))

    def get_min_avg_max_of_no_of_slides(self):
        print('Slides')
        print('Minimum no:of slides : ', min(self.no_of_slides.values()))
        total = len(self.no_of_slides.values())
        print('Average no:of slides : ', round(sum(self.no_of_slides.values()) / total,2))
        print('Maximum no:of slides : ', max(self.no_of_slides.values()))

    def get_biggest_climb(self):
        print('Biggest climb:',self.biggest_climb)

    def get_biggest_slide(self):
        print('Biggest slide:',self.biggest_slide)

    def get_unlucky_rolls(self):
        print('Unlucky Rolls')
        print('Minimum no:of unlucky rolls : ', min(self.unlucky_rolls.values()))
        total = len(self.unlucky_rolls.values())
        print('Average no:of unlucky rolls : ',round(sum(self.unlucky_rolls.values()) / total,2))
        print('Maximum no:of unlucky rolls : ', max(self.unlucky_rolls.values()))

    def get_lucky_rolls(self):
        print('Lucky Rolls')
        print('Minimum no:of lucky rolls : ', min(self.lucky_rolls.values()))
        total = len(self.lucky_rolls.values())
        print('Average no:of lucky rolls : ', round(sum(self.lucky_rolls.values()) / total,2))
        print('Maximum no:of lucky rolls : ', max(self.lucky_rolls.values()))

    def get_longest_turn(self):
        print('Longest Turn of 6\'s in each simulation',self.biggest_turn)

    def set_stats_longest_turn(self,biggest_six_turn,count):
        longest = max(biggest_six_turn)
        self.biggest_turn[count] = [biggest for biggest in biggest_six_turn if len(longest) == len(biggest)]

    def set_stats_rolls_to_win_and_lucky_rolls(self,count, dice_rolled, curr_position):
        self.rolls_to_win[count] += 1
        if curr_position >=94 and (dice_rolled + curr_position) == 100 :
            self.lucky_rolls[count] += 1

    def set_stats_for_climb(self,count,curr_position,ladder_end):
        distance_climbed = ladder_end - curr_position
        self.no_of_climbs[count] += distance_climbed

        if distance_climbed > self.biggest_climb[count]:
            self.biggest_climb[count] = distance_climbed
        self.lucky_rolls[count] += 1

    def set_stats_for_descends(self,count,curr_position,snake_end):
        distance_descended = curr_position - snake_end
        self.no_of_slides[count] += distance_descended

        if distance_descended > self.biggest_slide[count]:
            self.biggest_slide[count] = distance_descended

        self.unlucky_rolls[count] += 1

    def set_stats_for_lucky_rolls(self,count,snake_keys,curr_position):
        for snake in snake_keys:
            if abs(curr_position - snake) in [1, 2]:
                print('Got lucky, just missed a snake!')
                self.lucky_rolls[count] += 1
