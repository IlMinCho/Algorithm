import turtle
import random

def draw_hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)

def draw_rotated_hexagons(start_size, num_hexagons):
    for _ in range(num_hexagons):
        turtle.pensize(1)
        
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        turtle.color(random_color)
        draw_hexagon(start_size)
        turtle.right(360/num_hexagons)


turtle.speed(0)
turtle.bgcolor("black")
turtle.colormode(255) 

start_size = 120

draw_rotated_hexagons(start_size, 9)

turtle.hideturtle()
turtle.done()

