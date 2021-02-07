from snake import Snake
import time

snake = Snake()
game_is_on = True

while game_is_on:
    snake.move()
    snake.screen.listen()
    snake.screen.onkey(key="Up", fun=snake.up)
    snake.screen.onkey(key="Down", fun=snake.down)
    snake.screen.onkey(key="Left", fun=snake.left)
    snake.screen.onkey(key="Right", fun=snake.right)
