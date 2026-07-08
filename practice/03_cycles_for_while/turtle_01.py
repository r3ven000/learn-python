import turtle  
from data_sandbox import get_rainbow_colors

colors = get_rainbow_colors(100)
distances = range(100, 400, 2)  

turtle.bgcolor('black')
turtle.ht()
turtle.speed(10)

for color, distance in zip(colors, distances):  
    turtle.color(color)  
    turtle.forward(distance)  
    turtle.right(73)
    
turtle.done()
