import cv2
import numpy
import sys
import image_fixer
import simplifier
import os
from tqdm import tqdm
file=input("Enter the name of the image: ")
instantly=input("Do you want to instantly see the result? (y/n): ")

f = open("Turtlescript.py", "w")
f.write("from turtle import Screen\nimport turtle as Turtle\n")
f.write("screen = Screen()\nscreen.setup(700, 450)\nscreen.setworldcoordinates(-600, -385, 700, 450)\n")
if instantly=="y":
    f.write("screen.tracer(0)\n")
f.write("Turtle.speed(0)\n")
f.write("Turtle.penup()\n")
f.write("Turtle.goto(-300,300)\n")
f.write("Turtle.pendown()\n")
f.write("Turtle.colormode(255)   \n")
f.write("def skip():\n   Turtle.penup()\n   Turtle.forward(30)\n   Turtle.pendown()\n")
f.write('def drawpixel(pxcolor):\n      color = pxcolor\n      Turtle.color(color[0],color[1],color[2])\n      Turtle.pencolor(color[0],color[1],color[2])\n      Turtle.begin_fill()\n      for _ in range(4):\n        Turtle.forward(30)\n        Turtle.right(90)\n      Turtle.end_fill()\n      skip()\n')

numpy.set_printoptions(threshold=sys.maxsize)
filename=image_fixer.fix(file)
img=cv2.imread(filename)
row,col,ch=img.shape
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("Dimesions are: "+str(row)+" x "+str(col))
print("Generating...")

    
for i in tqdm(range(0,row)):
    for j in range(0,col):
        f.write("drawpixel(["+str(img[i][j][0])+","+str(img[i][j][1])+","+str(img[i][j][2])+"])\n")
    f.write("Turtle.penup()\n")
    f.write("Turtle.goto(-300,300-("+str(i)+"+1)*30)\n")
    f.write("Turtle.pendown()\n")
    
if instantly=="y":
    f.write("screen.update()\n")
    f.write("screen.mainloop()\n")

os.remove("img2.png")
print("Done! \nThe file is called Turtlescript.py")

f.close()
simplifier.simple("turtlescript.py")