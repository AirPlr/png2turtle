from PIL import Image
import PIL
def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True

    return False


def image_fixer(filename):
    img = Image.open(filename)
    if has_transparency(img):
        img = img.convert("RGB")
    img.save(filename)
    return filename

