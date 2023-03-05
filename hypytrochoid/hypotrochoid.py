import math
import turtle
from typing import Tuple
import time

class Hypotrochoid:
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [calculate_x(R, r, d, theta) for theta in self.thetas]
        self.y = [calculate_y(R, r, d, theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y, self.thetas))

    def trace(self, speed: int = 0, screen_size: Tuple[int, int] = (1000, 1000), exit_on_click: bool = False, color: str = "black", hide_turtle: bool = True) -> None:
        """Turtle draw the hypotrochoid"""
        screen = turtle.Screen()
        screen.setup(*screen_size)
        turtle.speed(speed)
        turtle.color(color)
        turtle.tracer(False)
        if hide_turtle:
            turtle.hideturtle()
        t3 = turtle.Turtle()
        t3.hideturtle()
        t3.speed(0)
        t3.pensize(2)
        t3.up()
        t3.seth(0)
        t3.goto(0,-self.R)
        t3.down()
        t3.circle(self.R,steps=200)


        shape_turtle = turtle.Turtle()
        shape_turtle.speed(1)
        small_circle_turtle = turtle.Turtle()
        small_circle_turtle.speed(1)
        small_circle_turtle.hideturtle()

        first = True 
        shape_turtle.up()
        for x, y, theta in self.coords:
            time.sleep(.1)
            shape_turtle.goto(x, y)

            small_circle_turtle.clear()
            small_circle_turtle.up()
            small_circle_y=(self.R - self.r)*math.sin(theta) - self.r
            small_circle_x=(self.R - self.r)*math.cos(theta)
            small_circle_turtle.goto(small_circle_x, small_circle_y)
            small_circle_turtle.down()
            small_circle_turtle.color("black")
            small_circle_turtle.circle(self.r,steps=200)

            # dist = -self.r*theta*math.pi/180
            # big_radian = dist/self.R

            # small_circle_turtle.seth(0)
            # small_circle_turtle.clear()
            # small_circle_turtle.up()
            # small_circle_turtle.goto(x, y)
            # small_circle_turtle.down()
            # small_circle_turtle.dot(10,'red')
            # small_circle_turtle.seth(theta)
            # small_circle_turtle.color("purple")
            # small_circle_turtle.bk(self.d)
            # small_circle_turtle.color("black")
            # small_circle_turtle.circle(self.r,steps=200)



            # turtle.clear()
            # turtle.up()
            # turtle.seth(0)
            # turtle.goto(x,y-self.r)
            # turtle.down()
            # turtle.color('black')
            # turtle.up()
            # turtle.goto(x,y)
            # turtle.dot(10,'blue')
            # turtle.down()

            if first:
                first = False
                shape_turtle.down()
            turtle.update()
        if exit_on_click:
            turtle.exitonclick()

def calculate_x(R: float, r: float, d: float, theta: float) -> float:
    """Return calculated x-value from parametrized equation"""
    return (R - r)*math.cos(theta) + d*math.cos(((R-r)/r)*theta)

def calculate_y(R: float, r: float, d: float, theta: float) -> float:
    """Return calculated y-value from parametrized equation"""
    return (R - r)*math.sin(theta) + d*math.sin(((R-r)/r)*theta)
