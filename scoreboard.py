from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def add_to_scoreboard(self, score):
        self.write(f"Scoreboard {score}", False, align="center", font=('Arial', 15, 'normal'))

    def game_over(self, score):
        self.goto(0, 0)
        self.write(f"Game over, your score is {score}", False, align="center", font=('Arial', 15, 'normal'))

    def clear_scoreboard(self):
        self.clear()
