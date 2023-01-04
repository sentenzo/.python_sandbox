from abc import ABC, abstractmethod
import random
import pickle

from flyweight import WordsDictionary


class Mumbler(ABC):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.dictionary = None

    @abstractmethod
    def _generate_random_text(self) -> str:
        l = random.choices([1, 2, 3], [3, 2, 1])
        return " ".join([self._generate_random_sentance() for _ in range(l)])

    def mumble(self) -> None:
        text = self._generate_random_text()
        print(f"[Mumbler {self.name}]: (mumbles) {text}")


class MumblerUnoptimized(Mumbler):
    def __init__(self, name) -> None:
        self.name = name
        self.dictionary = pickle.load(open("dictionary.p", "rb"))  # +50 Mb

    def _generate_random_text(self) -> str:
        l = random.choices([1, 2, 3], [3, 2, 1])[0]
        return " ".join([self._generate_random_sentance() for _ in range(l)])

    def _generate_random_sentance(self) -> str:
        sent = []
        pos = ""
        while pos != ".":
            if not pos in self.dictionary:
                break
            dd = self.dictionary[pos]
            next_pos = random.choices(dd[0], dd[1])[0]
            sent.append(next_pos)
            pos = next_pos

        return " ".join(sent)


class MumblerOptimized(Mumbler):

    def __init__(self, name) -> None:
        self.name = name
        self.dictionary = WordsDictionary("dictionary.p")

    def _generate_random_text(self) -> str:
        l = random.choices([1, 2, 3], [3, 2, 1])[0]
        return " ".join([self._generate_random_sentance() for _ in range(l)])

    def _generate_random_sentance(self) -> str:
        sent = []
        pos = ""
        while pos != ".":
            next_pos = self.dictionary.get_next_word(pos)
            sent.append(next_pos)
            pos = next_pos

        return " ".join(sent)