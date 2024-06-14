from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.score = 0
        self.color("White")
        self.penup()
        self.setpos(0,270)
        self.scoreboard()
        self.ht()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as high_score:
                high_score.write(f"{self.score}")
        self.score = 0
        self.scoreboard()

    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)

    def gain_point(self):
        self.score += 1
        self.scoreboard()



