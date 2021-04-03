from scoreboard import ScoreBoard
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()
    
    #Detect the collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update_score()
        
    
    # Detect collison with the wall    
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #game_is_on = False
        #score_board.game_over()
        score_board.reset()
        snake.reset()
        time.sleep(0.5)
        
    #Detect collison with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            score_board.reset()
            snake.reset()
            time.sleep(0.5)


screen.exitonclick()
