from PIL import Image
def fix(filename):
    img = Image.open(filename)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        
             # This is for checking white pixels, replace transparent. Do
        if item[3] == 0:
            newData.append((255, 255, 255, 255))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("img2.png", "PNG")
    return "img2.png"
