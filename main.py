from snake import Snake
from food import Food
from score import Score

#objects
snake = Snake()
food = Food()
score = Score()

#variables
game_is_on = True

#collision boarders
left = -280
right = 280
up = 280
down = -280


while game_is_on:
    snake.move()
    snake.screen.listen()
    snake.screen.onkey(key="Up", fun=snake.up)
    snake.screen.onkey(key="Down", fun=snake.down)
    snake.screen.onkey(key="Left", fun=snake.left)
    snake.screen.onkey(key="Right", fun=snake.right)

    #collision detection
    if snake.segments[0].distance(food) < 15:
        food.spawn_food()
        score.update_score()

    #detecting snake x&y pos
    x_pos = snake.segments[0].xcor()
    y_pos = snake.segments[0].ycor()

    if x_pos < left or x_pos > right or y_pos > up or y_pos < down:
        print("Game over")