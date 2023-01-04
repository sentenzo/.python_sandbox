import pickle
import re
from collections import defaultdict

text_soarces = ["корпус текстов.txt"]

dictionary = defaultdict(dict)

for path in text_soarces:
    with open(path, errors='ignore', encoding="utf-8") as txt:
        for line in txt.readlines():
            sents = re.split("[:\"'.\\?!]", line)
            sents = [s.strip() for s in sents]
            sents = [s for s in sents if s]
            for sent in sents:
                sent = re.split("[, ;-]", sent)
                sent = [s.strip() for s in sent]
                sent = [s for s in sent if s]
                if not sent:
                    continue
                last = sent.pop()
                dictionary[last]["."] = dictionary[last].get(".", 0) + 1
                if sent:
                    dictionary[""][sent[0]] = dictionary[""].get(
                        sent[0], 0) + 1
                    for i in range(1, len(sent)):
                        dictionary[sent[i-1]][sent[i]
                                              ] = dictionary[sent[i-1]].get(sent[i], 0) + 1

        new_dict = {}
        for w in dictionary:
            new_dict[w] = [[], []]
            for e in dictionary[w]:
                new_dict[w][0].append(e)
                new_dict[w][1].append(dictionary[w][e])

pickle.dump(new_dict, open("dictionary.p", "wb"))  # ~ 5 mb