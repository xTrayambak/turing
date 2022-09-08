import sys

from turing.image_gen import generate_captcha_image
from turing.core import CAPTCHA

d = CAPTCHA()
test = d.generate_test()
test.display_img()

are_you_a_robot = input('Enter what you see: ')

result = test.verify(are_you_a_robot)

if result == True:
    print('You are a human.')
else:
    print('You are a robot. Begone!')
