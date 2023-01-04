import pickle
import random

class WordsDictionary:
    wd_cache = {}

    def __init__(self, path: str) -> None:
        self.wd = None
        if not path in WordsDictionary.wd_cache:
            with open(path, "rb") as d:
                WordsDictionary.wd_cache[path] = pickle.load(d)
        self.wd = WordsDictionary.wd_cache[path]

    def get_next_word(self, word: str) -> str:
        if word in self.wd:
            dd = self.wd[word]
            return random.choices(dd[0], dd[1])[0]
        else:
            return "."