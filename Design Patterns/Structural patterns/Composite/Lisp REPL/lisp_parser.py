class Parser:
    @staticmethod
    def split(text):
        lexems = []
        words = text.split()
        i = 0
        while i < len(words):
            if words[i].startswith("("):
                sub_lexem = []
                while True:
                    sub_lexem.append(words[i])
                    if words[i].endswith(")"):
                        sub_lexem = " ".join(sub_lexem)
                        lexems.append(sub_lexem)
                        break
                    i += 1
            else:
                lexems.append(words[i])
            i += 1
        return lexems