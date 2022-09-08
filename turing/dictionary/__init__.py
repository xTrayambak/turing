import random
import requests
import os

class Dictionary:
    """
    Contains input for the random word generator.
    """
    def __init__(self):
        self.dictionary = []

        for _item in os.listdir('./nobot/dictionary/predefined'):
            if os.path.isfile('./nobot/dictionary/predefined/'+_item):
                self.add_file('./nobot/dictionary/predefined/'+_item)


    def add_file(self, file: str):
        with open(file, 'r') as new_file:
            for word in new_file.readlines():
                self.dictionary.append(word.split('\n')[0])


    def generate_text(self, count: int = None) -> str:
        if count is None:
            count = random.randint(2, 5)

        string = ''
        for _x in range(count):
            if _x != 0:
                string += ' '

            string += random.choice(self.dictionary)
 
        return string


    def add_api(self, url: str, keyword: str, pages: dict = [], params: dict = {}, count: int = 4):
        """
        Contact a web API `count` number of times. A lower value is recommended if you do not own the API, as you can DOS the servers.
        Increase `count` at your own risk.
        """
        for page in pages:
            for x in range(count):
                get_req = requests.get(url + '/' + page, params = params).json()[keyword]
                self.dictionary.append(get_req)

        if len(pages) == 0:
            for x in range(count):
                self.dictionary.append(requests.get(url, params = params).json())[keyword]
