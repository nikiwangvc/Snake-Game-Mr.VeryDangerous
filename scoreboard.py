from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def trackScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Uh Oh Mr. Very Dangerous, let's try again!", align=ALIGN, font=FONT)