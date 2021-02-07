from turtle import Turtle, Screen
import time


class Snake:

    def __init__(self):

        # initial variables
        self.start_position = 0
        self.segments = []
        self.game_is_on = True

        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake")
        self.screen.tracer(0)

        # create initial snake body
        for body_part in range(0, 3):
            # snake default settings
            new_segment = Turtle()
            new_segment.color("green")
            new_segment.shape("square")
            new_segment.shapesize()
            new_segment.penup()
            new_segment.goto(self.start_position, 0)
            self.start_position -= 20
            self.segments.append(new_segment)

    def move(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(1)

            for seg in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg - 1].xcor()
                new_y = self.segments[seg - 1].ycor()
                self.segments[seg].goto(new_x, new_y)
            self.segments[0].forward(20)
        self.screen.exitonclick()
