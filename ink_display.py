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
        self.Himage_draw = Image.new(
            "RGB", (self.ink.width, self.ink.height), self.ink.WHITE
        )
        self.draw = ImageDraw.Draw(self.Himage_draw)

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
        logging.info("sleeping for 15 seconds")
        time.sleep(15)
        self.font

    def clear_draw(self) -> None:
        logging.info("creating new draw image")
        self.Himage_draw = Image.new(
            "RGB", (self.ink.width, self.ink.height), self.ink.WHITE
        )
        self.draw = ImageDraw(self.Himage_draw)

    def draw_text(self, location, text, font, size, color) -> None:
        logging.info(f"writing text to draw image: {text}")
        self.draw.text(
            (location),
            text,
            ImageFont.truetype(os.path.join(FONT_DIR, font), size),
            color,
        )
        time.sleep(3)

    def display_draw(self) -> None:
        logging.info("displaying draw image")
        self.ink.display(self.ink.getbuffer(self.Himage_draw))
