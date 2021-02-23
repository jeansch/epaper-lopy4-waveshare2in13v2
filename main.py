from waveshare_epd import epd2in13_V2
from image import image

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)
epd.display(image)
