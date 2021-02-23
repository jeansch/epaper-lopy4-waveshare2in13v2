from PIL import Image


# Borrowed from waveshare python driver
# To be ran on the computer, not the controller
def getbuffer(width, height, image):
    if width % 8 == 0:
        linewidth = int(width / 8)
    else:
        linewidth = int(width / 8) + 1

    buf = [0xFF] * (linewidth * height)
    image_monocolor = image.convert('1')
    imwidth, imheight = image_monocolor.size
    pixels = image_monocolor.load()

    if(imwidth == width and imheight == height):
        for y in range(imheight):
            for x in range(imwidth):
                if pixels[x, y] == 0:
                    x = imwidth - x
                    buf[int(x / 8) + y * linewidth] &= ~(0x80 >> (x % 8))
    elif(imwidth == height and imheight == width):
        for y in range(imheight):
            for x in range(imwidth):
                newx = y
                newy = height - x - 1
                if pixels[x, y] == 0:
                    newy = imwidth - newy - 1
                    buf[int(newx / 8) + newy * linewidth] &= ~(0x80 >> (y % 8))
    return buf


open("image.py", "w").write(
    "image = %r\n" %
    getbuffer(122, 250, Image.open('2in13-v2.bmp')))
