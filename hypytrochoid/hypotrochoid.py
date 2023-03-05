import math
import turtle
from typing import Tuple

class Hypotrochoid:
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [calculate_x(R, r, d, theta) for theta in self.thetas]
        self.y = [calculate_y(R, r, d, theta) for theta in self.thetas]
        self.coords = list(zip(self.x, self.y))

    def trace(self, speed: int = 0, screen_size: Tuple[int, int] = (1000, 1000), exit_on_click: bool = False, color: str = "black", hide_turtle: bool = True) -> None:
        """Turtle draw the hypotrochoid"""
        screen = turtle.Screen()
        screen.setup(*screen_size)
        turtle.speed(speed)
        turtle.color(color)
        if hide_turtle:
            turtle.hideturtle()

        shape_turtle = turtle.Turtle()
        first = True 
        shape_turtle.up()
        for x, y in self.coords:
            shape_turtle.goto(x, y)
            if first:
                first = False
                shape_turtle.down()
        if exit_on_click:
            turtle.exitonclick()

def calculate_x(R: float, r: float, d: float, theta: float) -> float:
    """Return calculated x-value from parametrized equation"""
    return (R - r)*math.cos(theta) + d*math.cos(((R-r)/r)*theta)

def calculate_y(R: float, r: float, d: float, theta: float) -> float:
    """Return calculated y-value from parametrized equation"""
    return (R - r)*math.sin(theta) + d*math.sin(((R-r)/r)*theta)
