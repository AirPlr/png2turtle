import cv2
import numpy
import sys
import image_fixer
import simplifier
file=input("Enter the name of the image: ")
f = open("Turtlescript.py", "w")
f.write("from turtle import Screen\nimport turtle as Turtle\n")
f.write("screen = Screen()\nscreen.setup(700, 450)\nscreen.setworldcoordinates(-600, -385, 700, 450)\n")
f.write("screen.tracer(0)\n")
f.write("Turtle.speed(0)\n")
f.write("Turtle.penup()\n")
f.write("Turtle.goto(-300,300)\n")
f.write("Turtle.pendown()\n")
f.write("Turtle.colormode(255)   \n")
f.write("def skip():\n   Turtle.penup()\n   Turtle.forward(30)\n   Turtle.pendown()\n")
f.write('def drawpixel(pxcolor):\n   color = pxcolor\n   if color[0]!=0 or color[1]!=0 or color[2]!=0: \n      Turtle.color(color[0],color[1],color[2])\n      Turtle.pencolor(color[0],color[1],color[2])\n      Turtle.begin_fill()\n      for _ in range(4):\n        Turtle.forward(30)\n        Turtle.right(90)\n      Turtle.end_fill()\n   skip()\n')

numpy.set_printoptions(threshold=sys.maxsize)
filename=image_fixer.image_fixer(file)
img=cv2.imread(filename)
row,col,ch=img.shape
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(str(row)+" "+str(col))
print(img)

    
for i in range(0,row):
    for j in range(0,col):
        f.write("drawpixel(["+str(img[i][j][0])+","+str(img[i][j][1])+","+str(img[i][j][2])+"])\n")
    f.write("Turtle.penup()\n")
    f.write("Turtle.goto(-300,300-("+str(i)+"+1)*30)\n")
    f.write("Turtle.pendown()\n")
f.write("screen.update()\n")
f.write("screen.mainloop()\n")



f.close()
simplifier.simple("turtlescript.py")