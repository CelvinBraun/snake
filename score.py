from turtle import Turtle

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
        self.goto(0,text_height)
        self.score = 0
        self.write(arg=f"Your score: {self.score}", align="center", font=text_font)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Your score: {self.score}", align="center", font=text_font)

    def game_over(self):
        self.clear()
        self.goto(0,20)
        self.write(arg=f"GAME OVER!", align="center", font=text_font)
        self.goto(0, -20)
        self.write(arg=f"Your final score: {self.score}", align="center", font=text_font)