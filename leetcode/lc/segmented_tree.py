from typing import *


class SegmentTree:
    def __init__(self, nums: List[int]):
        xs = nums
        self.xs = xs
        l = len(nums)
        l2 = 1 << len(bin(l - 1)) - 2
        xs += [0] * (l2 - l)
        xss = [xs]
        nxt = lambda xs: list(map(sum, zip(xs[::2], xs[1::2])))
        while True:
            xss.append(nxt(xss[-1]))
            if len(xss[-1]) == 1:
                break
        self.xss = xss

    # """       *      *
    # [1, 3, 2, 3, 1, -4, 3, 2, 8, -12, 0, 0, 0, 0, 0, 0]
    # [  4,    5,    -3,    5,    -4,     0,    0,    0]
    # [      9,           2,          -4,          0]
    # [            11,                      -4]
    # [                         7]
    # 3 - 5 -9 -11
    # -4 - -3 - 2 - 11
    # """

    def update(self, index: int, val: int) -> None:
        i = index
        diff = val - self.xss[0][i]
        for z in range(len(self.xss)):
            self.xss[z][i] += diff
            i //= 2

    def running_sum(self, i):
        if i < 0:
            return 0
        b = bin(i)[2:]
        b = "0" * (len(self.xss) - len(b) - 1) + b
        z = len(self.xss) - 1
        i = 0
        ans = self.xss[z][i]
        for c in b:
            z -= 1
            if c == "0":
                i = i * 2
                ans -= self.xss[z][i + 1]
            else:
                i = i * 2 + 1
        return ans

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sum(right) - self.running_sum(left - 1)
