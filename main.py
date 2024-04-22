import ink_display as ink
import logging

logging.basicConfig(level=logging.DEBUG)

ink = ink.InkDisplay()
image = 'zelda00.bmp'
font = 'Font.ttc'

def main():
    try:
        # INIT/CLEAR
        ink.init()
        ink.clear()
        
        # DISPLAY IMAGE
        ink.display_image(image)
        ink.clear()
        
        # DISPLAY FONT
        ink.font(font, 24)
        ink.display_text(text="hello world", location=(5, 0), size=24, color="#FF0000")
        ink.clear()
        
        # DISPLAY DRAW
        # TODO: implement draw
        
        ink.sleep()
                    
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        ink.exit()
        exit()

main()