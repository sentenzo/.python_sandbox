from evaluatable import Evaluatable
import re


def init_func_repository():
    fr = {"+": lambda *args: sum(args),
          "-": lambda *args: 2 * args[0] - sum(args)}

    def prod(*args):
        ans = 1
        for arg in args:
            ans *= arg
        return ans

    def div(*args):
        x, *xs = args
        return x / prod(*xs)
    fr["*"] = prod
    fr["/"] = div

    def eq(*args):
        x, *xs = args
        for e in xs:
            if x != e:
                return False
        return True
    fr["="] = eq
    return fr


class Atom(Evaluatable): # feaf
    func_repository = init_func_repository()

    def __init__(self, word) -> None:
        word = word.strip()
        if not word in Atom.func_repository and not re.match(r"\w+", word):
            raise SyntaxError(f"Failed to init Atom object from \"{word}\"")
        self.word = word
        super().__init__()

    def eval(self) -> any:
        if self.word in Atom.func_repository:
            return Atom.func_repository[self.word]
        else:
            return int(self.word)