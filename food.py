
import random


class Food:
    def __init__(self):
        self.position = (0,0)

    def set_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        new_coordinate = (x,y)
        self.position = new_coordinate
        return self.position
