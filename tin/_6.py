DBG = True

INP = """
4
3
2
5
2
""".strip().split(
    "\n"
)


def _input():
    if DBG:
        return INP.pop(0)
    else:
        return input()


#################

from collections import defaultdict

TRIE = lambda: defaultdict(TRIE)


class Trie:
    def __init__(self, rank=32):
        self._trie = TRIE()
        self._rank = rank

    def add(self, xb):
        cur = self._trie
        r = self._rank
        zn = r - len(xb)
        while zn:
            zn -= 1
            cur = cur["0"]
        for d in xb:
            cur = cur[d]

    def get_best_pair(self, can):
        cur = self._trie
        r = self._rank
        zn = r - len(can)
        while zn:
            zn -= 1
            cur = cur["0"]
        ans = []
        for d in can:
            b = "0" if d == "1" else "1"
            nxt = b if b in cur else d
            ans.append(nxt)
            cur = cur[nxt]
        return "".join(ans)


n = int(_input())
trie = Trie()
mx = 0
while n > 0:
    n -= 1
    q = int(_input())
    qb = bin(q)[2:]
    trie.add(qb)
    pb = trie.get_best_pair(qb)
    p = int(pb, base=2)
    # print(q, p)
    mx = max(mx, p ^ q)
    print(mx)
