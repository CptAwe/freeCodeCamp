import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs) -> None:
        # random.seed() # Initialising random gives too much randomness and the tests fail, LOL!
        if not kwargs: raise ValueError("Can't have an empty hat...")
        self.contents = []
        for ball_color in kwargs:
            num_of_balls = kwargs[ball_color]
            self.contents.extend([ball_color]*num_of_balls)
        
        self.total_num_of_balls = len(self.contents)
    
    def __draw_one_random_ball(self) -> str:
        """return a random ball that was drawn from the hat"""
        pulled_ball_index = random.randint(0, self.total_num_of_balls - 1)
        picked_out_ball = self.contents.pop(pulled_ball_index)
        self.total_num_of_balls -= 1
        return picked_out_ball
    
    def draw(self, num_of_balls_to_draw: int) -> list:
        if num_of_balls_to_draw > self.total_num_of_balls:
            num_of_balls_to_draw = self.total_num_of_balls
        
        picked_out_balls = []
        for i in range(num_of_balls_to_draw):
            picked_out_balls.append(self.__draw_one_random_ball())
        return picked_out_balls


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments):

    def compare_results(results):
        for ball_colour in expected_balls:
            if expected_balls[ball_colour] > results.get(ball_colour, 0):
                return False
        return True
        
    successfull_experiments = 0
    for experiment_num in range(num_experiments):
        hat_of_interest = copy.deepcopy(hat)

        results = {}
        drawn_balls = hat_of_interest.draw(num_balls_drawn)
        for ball_colour in drawn_balls:
            if ball_colour in results:
                results[ball_colour] += 1
            else:
                results[ball_colour] = 1
            
            # Compare with the expected results
            if compare_results(results):
                # the experiment was successfull
                successfull_experiments += 1
                break
    
    probability = successfull_experiments/num_experiments
    return probability
