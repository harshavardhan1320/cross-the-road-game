import random
from turtle import Turtle
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVING_DISTANCE = 5


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 10

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_y = random.randint(-250, 250)
            new_car.goto(350, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVING_DISTANCE
