from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Helvetica", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()


    def update_score(self):
        self.score += 1
        self.update_scoreboard()