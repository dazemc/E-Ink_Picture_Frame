import sys
import os
from globals import *
import logging
from lib import epd7in3f
import time
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)


class InkDisplay:
    def __init__(self) -> None:
        self.ink = epd7in3f.EPD()

    def init(self) -> None:
        logging.info("initialising")
        if os.path.exists(LIB_DIR):
            sys.path.append(LIB_DIR)
        self.ink.init()

    def clear(self) -> None:
        logging.info("clearing screen")
        self.ink.Clear()

    def sleep(self) -> None:
        logging.info("putting to sleep")
        self.ink.sleep()

    def exit(self) -> None:
        logging.info("ctrl + c:")
        epd7in3f.epdconfig.module_exit()

    def display_image(self, image) -> None:
        logging.info("displaying image")
        Himage = Image.open(os.path.join(IMG_DIR, image))
        self.ink.display(self.ink.getbuffer(Himage))

    def blank_image(self) -> Image:
        logging.info("creating new draw image")
        return Image.new("RGB", (self.ink.width, self.ink.height), self.ink.WHITE)

    def draw(self, image) -> ImageDraw:
        return ImageDraw.Draw(image)

    def draw_text(self, location, text, font, size, color, draw) -> None:
        logging.info(f"drawing text to draw image: {text}")
        draw.text(
            (location),
            text=text,
            font=ImageFont.truetype(os.path.join(FONT_DIR, font), size),
            fill=color,
        )
        
    def display_draw(self, image) -> None:
        logging.info("displaying draw image")
        self.ink.display(self.ink.getbuffer(image))
