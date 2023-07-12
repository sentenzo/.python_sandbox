from __future__ import annotations

from enum import Enum

from random import randint


class Dice:
    def __init__(self, value: int, times: int = 1) -> None:
        self.value = value
        self.times = times

    def roll(self) -> int:
        return sum(randint(1, self.value) for _ in range(self.times))

    def __mul__(self, number: int) -> Dice:
        if self.times != 1:
            raise ValueError("Only the 1dn dice can be multiplied!")
        return Dice(self.value, self.times * number)

    __rmul__ = __mul__

    def __repr__(self) -> str:
        return f"{self.times}d{self.value}"


class D20Result(Enum):
    AUTO_FAILURE = 1
    _2 = 2
    _3 = 3
    _4 = 4
    _5 = 5
    _6 = 6
    _7 = 7
    _8 = 8
    _9 = 9
    _10 = 10
    _11 = 11
    _12 = 12
    _13 = 13
    _14 = 14
    _15 = 15
    _16 = 16
    _17 = 17
    _18 = 18
    _19 = 19
    AUTO_SUCCESS = 20


def roll_d20():
    return D20Result(randint(1, 20))


d1 = Dice(1)
d2 = Dice(2)
d3 = Dice(3)
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)


if __name__ == "__main__":
    print(
        *[d1, d2, d3, d4, d6, d8, d10, d12, 2 * d4, d6 * 2],
        sep="\n",
    )
