from turtle import Turtle
import time

#scoreboard settings
text_color = "white"
text_height = 280
text_font = "courier"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(text_color)
        self.speed("fastest")
        self.score = 0
        self.highscore = 0
        self.update_board()

    def update_board(self):
        self.clear()
        self.goto(0, text_height)
        self.write(arg=f"Score: {self.score} | Highscore: {self.highscore}", align="center", font=text_font)

    def increase_score(self):
        self.score += 1
        self.update_board()

    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.clear()
        self.update_board()
        self.goto(0,0)
        self.write(arg=f"GAME OVER!", align="center", font=text_font)
        time.sleep(5)
        self.update_board()