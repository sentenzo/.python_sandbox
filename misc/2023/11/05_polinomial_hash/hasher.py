HASHES = (
    (1499, 65537),
    (1997, 1114111),
    (1009, 10**9 + 7),
) # ((x, mod), ...)

CH2I = [ch + 17 for ch in range(256)]

class Polinomer:
    def __init__(self, string: str, x: int, mod: int) -> None:
        self.s = string
        self.x = x
        self.mod = mod

        self.cache_poli = [None] * (len(string)+1)
        self.cache_poli[0] = 0
        self.cache_poli[1] = CH2I[ord(string[0])]
        self.last = 1

        self.cache_pow = {}

    def _pow_x(self, exp):
        base = self.x
        mod = self.mod
        if  exp not in self.cache_pow:
            if exp < 2:
                self.cache_pow[exp] = (1, base % mod)[exp]
            else:
                d, m = divmod(exp, 2)
                self.cache_pow[exp] = self._pow_x(d) * self._pow_x(d+m) % mod # O(log(n))
        return self.cache_pow[exp]

    def polinomial(self, right, shift=0):
        s = self.s
        x = self.x
        mod = self.mod
        if self.cache_poli[right] is None:
            last = self.last
            for i in range(last+1, right+1):
                chi = CH2I[ord(s[i-1])]
                self.cache_poli[i] = (self.cache_poli[i-1] * x + chi) % mod
            self.last = right
        ans = self.cache_poli[right]
        ans *= self._pow_x(shift)
        ans %= mod
        return ans


class Hasher:
    def __init__(self, string: str, id_hash=False) -> None:
        self.cache_hash = {}
        
        self.s = string
        polis = []
        for x, m in HASHES:
            polis.append(Polinomer(string, x, m))
        self.polis = polis

        self.n = len(string)
        self.id_hash = id_hash


    def hash(self, i, left, right):
        key = (i, left, right)
        if key not in self.cache_hash:
            p: Polinomer = self.polis[i]
            _, mod = HASHES[i]
            poli_l = p.polinomial(left, right - left)
            poli_r = p.polinomial(right)
            hash = (poli_r - poli_l) % mod
            self.cache_hash[key] = hash

        return self.cache_hash[key]

    def gen_keys(self, left, right):
        for i in range(len(HASHES)):
            yield self.hash(i, left, right)
        if self.id_hash:
            yield self.s[left:right]

    def check_equality(self, a_start, a_end, b_start, b_end):
        gen_a = self.gen_keys(a_start, a_end)
        gen_b = self.gen_keys(b_start, b_end)
        try:
            while True:
                ha = next(gen_a)
                hb = next(gen_b)
                if ha != hb:
                    return False
        except StopIteration:
            return True

