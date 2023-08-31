from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
COLOR = ['yellow', 'green', 'blue']
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments = []

        # self.head_pos = (0, 0)
        self.create_snake()
        self.snake_head = self.segments[0]

    def update_length(self):
        self.length += 1

    def update_head_pos(self, new_position):
        pass

    def create_snake(self):
        for i in range(0, 3):
            tim = Turtle()
            tim.shape("square")
            tim.penup()
            tim.color(COLOR[i])
            tim.goto(STARTING_POS[i])
            tim.speed('fast')
            self.segments.append(tim)
        return self.segments

    def add_segment(self, segments):
        pass

    def move_snake(self):

        for seg in range(2, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.snake_head.forward(20)
        # self.update_head_pos(self.segments[0].pos())

        if self.snake_head.xcor() >= 285 or self.snake_head.xcor() <= -301 or self.snake_head.ycor() >= 285 or self.snake_head.ycor() <= -285:
            return False
        else:
            return True

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT :
            self.snake_head.setheading(RIGHT)
