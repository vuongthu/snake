from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())  # Need to convert it into an integer
        self.color("white")
        self.penup()
        self.goto(0, 370)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        # Added clear here because previously, we wanted to keep the score on the screen when it was game over
        # Now, we don't need to call it twice in increase_score or reset methods
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # Day 24, replacing the game over method with a new method
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")  # Rewrite it into the text file, used score here initially
        self.score = 0
        self.update_scoreboard()
