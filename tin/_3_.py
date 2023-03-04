DBG = True


def _input(val):
    if DBG:
        return val
    else:
        return input()


x = int(_input("9"))

m = x // 2

for a in range(m, 0, -1):
    b = x - a
    if b % a == 0:
        print(a, b)
        break
