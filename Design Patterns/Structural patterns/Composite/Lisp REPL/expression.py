from typing import List
from evaluatable import Evaluatable
from atom import Atom
from lisp_parser import Parser

class Expression(Evaluatable): # composite
    def __init__(self, text) -> None:
        self.children: List[Expression] = []
        text = text.strip()[1:-1]
        lexems = Parser.split(text)
        for lex in lexems:
            if lex.startswith("("):
                self.children.append(Expression(lex))
            else:
                self.children.append(Atom(lex))
        super().__init__()

    def eval(self) -> any:
        x, *xs = self.children
        ans = x.eval()
        if xs:
            args = []
            for x in xs:
                args.append(x.eval())
            ans = ans.__call__(*args)
        return ans