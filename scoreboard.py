from turtle import Turtle
ALIGNMENT = "center"
FONT = ("serif", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety(275)
        self.pencolor("pale violet red")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.pencolor("crimson")
        self.sety(50)
        self.write(arg="Game Over Loser, You aren't the GOAT", move=False, align="center", font=("serif", 12, "normal"))

    def quit(self):
        self.bye()