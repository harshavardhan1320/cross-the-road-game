from turtle import Screen
from buddy import Buddy
from cars import Car
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title("Turtle Cross")
screen.tracer(0)

t = Buddy()

car = Car()

score_board = ScoreBoard()

screen.listen()
screen.onkey(t.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    car.create_car()
    car.move()

    for c in car.all_cars:
        if c.distance(t) < 20:
            game_is_on = False
            score_board.game_over()

    finish = t.is_at_finish_line()
    if finish:
        t.go_to_start()
        car.level_up()
        score_board.increase_level()




screen.exitonclick()
