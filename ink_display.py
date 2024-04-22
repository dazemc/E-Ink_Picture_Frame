import sys
import os
from globals import *
import logging
from lib import epd7in3f
import time
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

class InkDisplay:
    def __init__(self) -> None:
        self.ink = epd7in3f.EPD()
        if os.path.exists(LIB_DIR):
            sys.path.append(LIB_DIR)
    
    def init(self) -> None:
        logging.info("initialising")
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
