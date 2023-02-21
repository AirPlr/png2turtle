import customtkinter
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
from tkinter.filedialog import askopenfilename
import cv2
import numpy
import sys
import image_fixer
import simplifier
import os
app = customtkinter.CTk()
app.geometry("600x480")
app.title("png2turtle")
file=""
instantly="n"
def button_callback():
    global file
    file=askopenfilename(filetypes=[("images",".png")])
    label_1.configure(text="Selected file: "+file)
    
def setinsta():
    global instantly
    instantly="y"  
    
def generate():
    gener(file, instantly)


def gener(file, instantly):
    
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
    dims="Dimesions are: "+str(row)+" x "+str(col)+"\n"
    label_2.configure(text=label_2.cget("text")+dims)
    gnt="Generating...\n"
    label_2.configure(text=label_2.cget("text")+gnt)
    
    for i in range(0,row):
        progressbar_1.set((i*100)/22)
        for j in range(0,col):
            f.write("drawpixel(["+str(img[i][j][0])+","+str(img[i][j][1])+","+str(img[i][j][2])+"])\n")
        f.write("Turtle.penup()\n")
        f.write("Turtle.goto(-300,300-("+str(i)+"+1)*30)\n")
        f.write("Turtle.pendown()\n")
    
    if instantly=="y":
        f.write("screen.update()\n")
        f.write("screen.mainloop()\n")

    os.remove("img2.png")
    label_2.configure(text=label_2.cget("text")+"Done! \nThe file is called Turtlescript.py")

    f.close()
    simplifier.simple("Turtlescript.py")
    
    
    

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60,fill="both", expand=True)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback, text="Choose file")
button_1.pack(pady=10, padx=10)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="File not selected")
label_1.pack(pady=10, padx=10)

inst_1 = customtkinter.CTkCheckBox(master=frame_1, text="Quick Print", command=setinsta)
inst_1.pack(pady=10, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1, mode="determinate")
progressbar_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=generate, text="Generate")
button_1.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Terminal Output:\n")
label_2.pack(pady=10, padx=10)
app.mainloop()
