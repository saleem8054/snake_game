import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()        
    
    def refresh(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))
