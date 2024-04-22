import ink_display as ink
import logging

logging.basicConfig(level=logging.DEBUG)

ink = ink.InkDisplay()
image = 'zelda00.bmp'
font = 'Font.ttc'

def main():
    try:
        ink.init()
        ink.clear()
        ink.display_image(image)
        ink.clear()
        ink.font(font, 24)
        ink.display_text("hello world", (5, 0), 24, ink.ink.RED)
        ink.clear()
        ink.sleep()
                    
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        ink.exit()
        exit()

main()