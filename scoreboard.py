from turtle import Turtle
FONT = ("Courier", 20, 'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(0,280)
        self.penup()
        self.pencolor('white')
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.clear()
        self.goto(0, 280)
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
