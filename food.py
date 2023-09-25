from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # We're only able to use the methods below because we are inheriting directly from the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("LightSalmon")
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-370, 370)
        random_y = random.randint(-370, 370)
        self.goto(random_x, random_y)
