from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import os
import sys

screen = Screen()
screen.setup(width=612, height=612)
screen.bgcolor("black")
screen.title("PahlawanJoey's Snake Game")
screen.tracer(0)

game_on = True
scoreboard = Scoreboard()
screen.listen()
food = Food()
snake = Snake()
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.move_left)
screen.onkeypress(key="Right", fun=snake.move_right)
screen.onkeypress(key="w", fun=snake.move_up)
screen.onkeypress(key="s", fun=snake.move_down)
screen.onkeypress(key="a", fun=snake.move_left)
screen.onkeypress(key="d", fun=snake.move_right)

def again():
    os.execl(sys.executable, sys.executable, *sys.argv)

def ask_play_again():
    value = screen.textinput(title="Play again?", prompt="Type Y of N").lower()
    if value == "y" or value == "ok":
        return True
    else:
        scoreboard.quit()

while game_on:
    screen.update()
    time.sleep(0.1)
    if not abs(snake.last_direction - snake.snake_segments[0].heading()) == 180:
        pass
    else:
        snake.snake_segments[0].setheading(snake.last_direction)
    snake.move_snake()
    if snake.snake_segments[0].distance(food) < 16:
        scoreboard.update_score()
        snake.extend_snake()
        food.respawn_food()
    if abs(snake.snake_segments[0].xcor()) > screen.window_width() // 2 or abs(
            snake.snake_segments[0].ycor()) > screen.window_height() // 2:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
        if ask_play_again():
            again()
    for bodypart in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(bodypart) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()
            if ask_play_again():
                again()
screen.exitonclick()
