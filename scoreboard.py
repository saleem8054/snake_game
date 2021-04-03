from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscores.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.color("white")
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score: {self.high_score}",align="center",font=("Arial", 12, "normal"))
           
    def reset(self): 
       if self.score > self.high_score:
           self.high_score = self.score
           with open("highscores.txt","w") as file:
               file.write(f"{self.high_score}")
       self.score = 0
       self.update_scoreboard()
   
    def update_score(self):
        self.score += 1
        self.update_scoreboard()
        
