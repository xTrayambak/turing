# Turing, a lightweight CAPTCHA-like library to detect whether your users are humans or not!
Because, you can never be too sure!
___________
# Usage
This is a basic way of generating a CAPTCHA.
```python3
from nobot.core import Test

my_captcha = Test(case_sensitive = False, strictness = 2)

captcha_img = my_captcha.generate_img()

captcha_img.save('mycaptchaimg', format = 'png')
```
__________
# Why use Turing over something else?
* Turing is a 100% Pythonic library. It follows PEP-8 (most of the time). So, your odds of being cyberbullied by a veteran Pythonista are very low.

* Turing does not use fancy AI or anything to test whether your users are a robot or not, making it very fast, light, and plug-and-play esque.

* We have a huge library of words, which is also being constantly updated. If you find it insufficient, you can always use an online API, and the `turing.dictionary.Dictionary` class has full support for it.

* And best of all, it does not use your users' data to build self-driving cars that crash into a wall 99% of the time. (wink wink, we all know who does that.)
___________
# Roadmap
* Add image distortion based on strictness level.
* Add audio support, possibly via FFMPEG.
* Extract the most performance out of the code as possible.
___________
# Where's the random word dictionary?
You can add your own dictionary set of random words using `turing.core.Test.add_dictionary()`,
if you want to use an online API for this, then you can use `turing.core.Test.add_dictionary_from_api(url = 'myurl.xyz', pages = ['/generate_random_words'], params = {'api_key': 'TEST123'})`

___________
# How do I raise the difficulty?
Raising the `strictness` attribute (which is an int) will add random lines between the text, and the line count will increase with the level of strictness. Audio will also be distorted accordingly, with level 0 having no distortion in either audio and image and level 10 will be near impossible to clear, even for a robot.

___________
# Contribution
You are welcome to contribute, but improvements to features, bug fixes are accepted rather than new features. For them, you can simply open a new Issue and if I cannot implement the feature (which is not likely), then you can feel free to implement the feature yourself.

____________
# Contacting Me
You can contact me at:
* Mail: xtrayambak@gmail.com
* Discord: xTrayambak#8956
* Twitter: @HelloImTray

Suggestions, bugs, and other reports are to be made in the Issues tab, however.
Please disclose vulnerabilities to be in private on either my Discord or Email rather than opening an issue, but feel free to open an issue once I tell you everything is clear.
