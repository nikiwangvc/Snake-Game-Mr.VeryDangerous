from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Feed your pet snake Mr. Very Dangerous the Python")
screen.tracer(0)

# OOP
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# have the screen to listen keypress
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

head = snake.segments[0]

game_is_on = True
while game_is_on:
    # to tell the screen to update everytime
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with wall
    if head.xcor() >= 300 or head.xcor() <= -300 or head.ycor() >= 300 or head.ycor() <= -300:
        game_is_on = False
        scoreboard.gameOver()

    # detect collision with food
    if head.distance(food) < 20:
        food.refresh()
        snake.grow()
        scoreboard.trackScore()
    # detect collision with itself
    # python slicing
    for i in snake.segments[1:]:
        if head.distance(i) < 15:
            game_is_on = False
            scoreboard.gameOver()


screen.exitonclick()
