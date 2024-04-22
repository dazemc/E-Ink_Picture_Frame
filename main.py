import ink_display as ink
import logging

logging.basicConfig(level=logging.DEBUG)

ink = ink.InkDisplay()
image = "zelda00.bmp"
font = "Font.ttc"


def main():
    try:
        # INIT/CLEAR
        ink.init()
        ink.clear()

        # DISPLAY IMAGE
        # ink.display_image(image)
        # ink.clear()

        # CREATE DRAW
        draw_image = ink.blank_image()
        ink.draw_text(
            (5, 0), text="hello", font=font, size=24, color="#FF0000", image=draw_image
        )
        ink.draw_text(
            (5, 30), text="world", font=font, size=16, color="#FF0000", image=draw_image
        )
        ink.draw(draw_image).line((5, 170, 80, 245), fill="#0000FF")
        ink.display_draw(draw_image)
        ink.clear()

        # CREATE NEW DRAW
        draw_image = ink.blank_image()
        ink.draw_text(
            (5, 0),
            text="goodbye world",
            font=font,
            size=36,
            color="#00FF00",
            image=draw_image,
        )
        ink.display_draw(draw_image)
        ink.clear()

        # SLEEP
        ink.sleep()

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        ink.exit()
        exit()


main()
