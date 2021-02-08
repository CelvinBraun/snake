from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.spawn_food()

    def spawn_food(self):
        food_spawn_width = random.randint(-280, 280)
        food_spawn_height = random.randint(-280, 280)
        self.goto(food_spawn_width, food_spawn_width)