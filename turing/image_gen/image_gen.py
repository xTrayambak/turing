import numpy

from random import randint, choice
from PIL import Image, ImageDraw, ImageFont

LINES_COLORS = ['red', 'blue', 'green', 'yellow', 'purple']

def captcha_gen_difficulty_lines(draw: ImageDraw, img_size: tuple, strictness: int):
    """
    Distorts the image according to the strictness level by adding lines, in order to confuse text-detection APIs.
    """
    if strictness == 0: return

    _strictness = strictness ** 2

    for line_draw in range(_strictness, _strictness + randint(1, _strictness)):
        x1 = randint( 0, img_size[1] + 1 )
        y1 = randint( 0, img_size[1] + 1 )

        x2 = randint( 0, img_size[1] + 1 )
        y2 = randint( 0, img_size[1] + 1 )

        xy = [(x1, y1), (x2, y2)]

        draw.line(xy, fill = choice(LINES_COLORS), width = 1)


def captcha_gen_difficulty_distort(image: Image, draw: ImageDraw, strictness: int):
    """
    Adapted from https://stackoverflow.com/questions/21940911/python-image-distortion
    """
    if strictness == 0: return image

    array = numpy.asarray(image)
    a_zeros = numpy.zeros((image.size[0], image.size[1], 3))

    a = array.shape[0] / 3.0
    w = 1.0 / array.shape[1]

    sine_shift = lambda x: a * numpy.sin(2.0 * numpy.pi * x * w)

    for x in range(array.shape[0]):
        a_zeros[:, x] = numpy.roll(array[:, 1], int(sine_shift(x)))

    return Image.fromarray(numpy.uint8(a_zeros))


def generate_captcha_image(text: str, font: str = None,
                           font_size: int = None, strictness: int = 0,
                           img_size: tuple = (256, 256), text_color: tuple = None,
                           bg_color: tuple = None) -> Image:
    """
    Generate text with the font provided, and distort it according to the strictness provided.

    :: args ::
    text: str - The text to show in the CAPTCHA
    font: str - The font to use
    strictness: int - The distortion level
    size: tuple [int, int] - The size of the image
    """
    if bg_color is None:
        bg_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    if text_color is None:
        text_color = (randint(0, 255), randint(0, 255), randint(0, 255))

    image = Image.new('RGB', img_size, bg_color)

    if font is not None:
        if font_size is None:
            font_size = random.randint(5, 10)

        font = ImageFont.truetype(font, font_size)

    draw = ImageDraw.Draw(image)
    draw.text(
        (randint(5, 180), randint(5, 180)),
        text = text, font = font, fill = text_color
    )

    # Apply final transformations
    captcha_gen_difficulty_lines(draw, img_size, strictness)
    #image = captcha_gen_difficulty_distort(image, draw, strictness)

    #image.show()
    return image
