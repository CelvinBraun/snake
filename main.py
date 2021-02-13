from snake import Snake
from food import Food
from score import Score
import time

#objects
snake = Snake()
food = Food()
score = Score()

#variables
game_is_on = True
programm_is_running = True

#collision boarders
left = -280
right = 280
up = 280
down = -280

while programm_is_running:

    while game_is_on:

        # detecting: when head collsion with body
        for part in range(1, len(snake.segments)):
            if snake.segments[0].distance(snake.segments[part]) < 15:
                game_is_on = False

        snake.move()
        snake.screen.listen()
        snake.screen.onkey(key="Up", fun=snake.up)
        snake.screen.onkey(key="Down", fun=snake.down)
        snake.screen.onkey(key="Left", fun=snake.left)
        snake.screen.onkey(key="Right", fun=snake.right)

        #collision detection
        if snake.segments[0].distance(food) < 15:
            food.spawn_food()
            x_pos = snake.segments[-1].xcor()
            y_pos = snake.segments[-1].ycor()
            snake.extend_snake(x_pos, y_pos)
            score.increase_score()

        # detecting snake x&y pos
        x_pos = snake.segments[0].xcor()
        y_pos = snake.segments[0].ycor()

        # when over boarder -> game over
        if x_pos < left or x_pos > right or y_pos > up or y_pos < down:
            game_is_on = False

    score.game_over()
    game_is_on = True
    snake.reset()
snake.screen.exitonclick()