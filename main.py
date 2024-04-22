import ink_display as ink
import logging

logging.basicConfig(level=logging.DEBUG)

ink = ink.InkDisplay()
image = 'zelda00.bmp'

def main():
    try:
        ink.init()
        ink.clear()
        ink.display_image(image)
                    
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        ink.exit()
        exit()