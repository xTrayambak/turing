from nobot.image_gen import generate_captcha_image
from nobot.dictionary import Dictionary

class Test:
    def __init__(self, dictionary, case_sensitive: bool = True, text: str = None, strictness: int = 4):
        if text is None:
            text = dictionary.generate_text()

        self.text = text
        self.img = generate_captcha_image(text = text, strictness = strictness)
        self.case_sensitive = case_sensitive


    def verify(self, answer: str) -> bool:
        if self.case_sensitive:
            return answer == self.text
        else:
            return answer.lower() == self.text.lower()


    def get_img(self):
        return self.img


    def display_img(self):
        self.img.show()

class CAPTCHA:
    def __init__(self, case_sensitive: bool = True, strictness: int = 4):
        self.dictionary = Dictionary()
        self.strictness = strictness
        self.tracked_tests = {}
        self.case_sensitive = case_sensitive


    def generate_test(self, text: str = None):
        test = Test(self.dictionary, self.case_sensitive, text, self.strictness)

        return test
