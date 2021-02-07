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


class Snake:

    def __init__(self):

        # initial variables
        self.start_position = 0
        self.segments = []
        self.game_is_on = True

        self.screen = Screen()
        self.screen.setup(width=screen_width, height=screen_height)
        self.screen.bgcolor(background_color)
        self.screen.title(window_title)
        self.screen.tracer(0)

        # create initial snake body
        for body_part in range(0, 3):
            # snake default settings
            new_segment = Turtle()
            new_segment.color(color_of_snake)
            new_segment.shape(shape_of_snake)
            new_segment.shapesize(size_of_snake)
            new_segment.penup()
            new_segment.goto(self.start_position, 0)
            self.start_position -= 20
            self.segments.append(new_segment)

    def move(self):
        self.screen.update()
        time.sleep(move_speed)

        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(move_distance)