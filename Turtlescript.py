from turtle import Screen
import turtle as Turtle
screen = Screen()
screen.setup(700, 450)
screen.setworldcoordinates(-600, -385, 700, 450)
Turtle.speed(0)
Turtle.penup()
Turtle.goto(-300,300)
Turtle.pendown()
Turtle.colormode(255)   
def skip():
   Turtle.penup()
   Turtle.forward(30)
   Turtle.pendown()
def drawpixel(pxcolor):
      color = pxcolor
      Turtle.color(color[0],color[1],color[2])
      Turtle.pencolor(color[0],color[1],color[2])
      Turtle.begin_fill()
      for _ in range(4):
        Turtle.forward(30)
        Turtle.right(90)
      Turtle.end_fill()
      skip()
