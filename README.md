# png2turtle
### Seems like no one made it, so this is my take to it

---

This script converts PNG and JPG files to Python Turtle Graphics
If you want to impress someone, this is the way to go

# BIG **ISSUES!**
* Does not render **black**
* Transparent is seen as `0,0,0` (**Black**) so it's not rendered
* The final drawing doesn't display properly

## To-Do
* Fix black
    - Making another script to modify the files
* Make the output simpler
    - `From: skip() skip() skip()` To `for i in range(3): skip()` or `skip(3)`
* Add comments

## Dependecies
Run this command
    `pip3 install opencv-python Turtle numpy`
    
# Running it!
Enter the name of your png or jpg file when asked:
`Enter the name of the image: g.png`
