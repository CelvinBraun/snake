from turtle import Turtle, Screen
import time

#game settings
window_title = "snake"
background_color = "black"
screen_width = 600
screen_height = 600
move_speed = 0.3

#snake settings
color_of_snake = "green"
shape_of_snake = "square"
size_of_snake = 1
move_distance = 20

#directions
up = 90
left = 180
down = 270
right = 0


class Snake:

    def __init__(self):

        # initial variables
        self.start_pos_x = 0
        self.start_pos_y = 0
        self.segments = []
        self.game_is_on = True

        # screen variables
        self.screen = Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.screen.bgcolor(background_color)
        self.screen.title(window_title)
        self.screen.tracer(0)
        self.create_snake()

    # create initial snake body
    def create_snake(self):
        for body_part in range(0, 3):
            self.add_segment()

    # add segement to snake
    def add_segment(self):
        new_segment = Turtle()
        new_segment.color(color_of_snake)
        new_segment.shape(shape_of_snake)
        new_segment.shapesize(size_of_snake)
        new_segment.penup()
        new_segment.goto(self.start_pos_x, self.start_pos_y)
        self.start_pos_x -= 20
        self.segments.append(new_segment)

    def extend_snake(self, pos_x, pos_y):
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.add_segment()

    def move(self):
        self.screen.update()
        time.sleep(move_speed)

        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)

    def reset(self):
        self.start_pos_x = 0
        self.start_pos_y = 0
        for seg in range(len(self.segments)):
            self.segments[seg].reset()
        self.segments.clear()
        self.create_snake()

#move directions
    def up(self):
        heading = self.segments[0].heading()
        if heading != down:
            self.segments[0].setheading(up)

    def down(self):
        heading = self.segments[0].heading()
        if heading != up:
            self.segments[0].setheading(down)

    def left(self):
        heading = self.segments[0].heading()
        if heading != right:
            self.segments[0].setheading(left)

    def right(self):
        heading = self.segments[0].heading()
        if heading != left:
            self.segments[0].setheading(right)