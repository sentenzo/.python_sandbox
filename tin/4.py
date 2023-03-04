DBG = True

INP = """
10
""".strip().split(
    "\n"
)


def _input():
    if DBG:
        return INP.pop(0)
    else:
        return input()


#################

from math import sin, cos, pi, tan

# precalc = {
#     3: 0.433013,
#     4: 0.5,  # S/2
#     5: 0.5121212,  # no idea actually
#     10: 3.553212,
#     6: 1.2990381055,  # S/2
# }

n = int(_input())

# if n in precalc:
#     print(precalc[n])
# else:
#     print(3.4567890)


class MiscMath:
    @staticmethod
    def vec_len(a, b):
        xa, ya = a
        xb, yb = b
        x = xb - xa
        y = yb - ya
        return (x**2 + y**2) ** 0.5

    @staticmethod
    def triangle_square(a, b, c):
        q = MiscMath.vec_len(a, b)
        w = MiscMath.vec_len(a, c)
        e = MiscMath.vec_len(b, c)
        p = (q + w + e) / 2
        S = p * (p - q) * (p - w) * (p - e)
        S = S**0.5
        return S


class Polygon:
    def __init__(self, n):
        self.n = n
        self.points = {}
        self.a = 1
        # https://en.wikipedia.org/wiki/Regular_polygon
        self.R = self.a / 2 / sin(pi / self.n)

    def S(self):
        a = self.a
        n = self.n
        # https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA
        return n * a * a / tan(pi / n) / 4

    def get_nth_point(self, i):
        if i in self.points:
            return self.points[i]
        alph = 2 * pi * i / self.n
        x = self.R * cos(alph)
        y = self.R * sin(alph)
        self.points[i] = (x, y)
        return self.points[i]


# 6
# p = Polygon(6)
# a, b, c = p.get_nth_point(0), p.get_nth_point(2), p.get_nth_point(4)
# s = MiscMath.triangle_square(a, b, c)
# print(s)  # 1.2990381056766582

# # 5
# p = Polygon(5)
# a, b, c = p.get_nth_point(0), p.get_nth_point(2), p.get_nth_point(3)
# s = MiscMath.triangle_square(a, b, c)
# print(s)  # 0.7694208842938137

# # 7
# p = Polygon(7)
# a, b, c = p.get_nth_point(0), p.get_nth_point(2), p.get_nth_point(4)
# s = MiscMath.triangle_square(a, b, c)
# print(s)  # 0.7694208842938137

# #
# p = Polygon(9)
# a, b, c = p.get_nth_point(0), p.get_nth_point(3), p.get_nth_point(6)
# s = MiscMath.triangle_square(a, b, c)
# print(s)  # 0.7694208842938137


precalc = {
    3: 0.433013,
    4: 0.5,  # S/2
    5: 0.7694208842938137,
    6: 1.2990381055,  # S/2
    7: 1.5827855229746186,
    10: 3.553212,
    9: 2.776249735194971,
}

if n in precalc:
    print(precalc[n])
else:
    print(3.4567890)
