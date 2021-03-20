from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_segments()
        self.head = self.snake[0]
        
        
    def create_segments(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)
        
        
    def add_segments(self,position):
        turtle = Turtle("square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)        
        self.snake.append(turtle)

    def extend(self):
        self.add_segments(self.snake[-1].position())
        
        
    def move(self):
        for seg_num in range(len(self.snake) - 1, 0 , -1):
            new_x = self.snake[seg_num-1].xcor()
            new_y = self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        
                
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

        