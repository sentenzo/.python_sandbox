DBG = True

INP = """
12 21 53
3023 565 10044
""".strip().split(
    "\n"
)


def _input():
    if DBG:
        return INP.pop(0)
    else:
        return input()


#################


cs = list(map(int, _input().split()))
vs = list(map(int, _input().split()))


def step(state, frm, to, all=False):
    _vs = list(state)
    fc = cs[frm]
    tc = cs[to]
    if fc > _vs[frm]:
        return False, _vs
    n = _vs[frm] // fc if all else 1
    _vs[frm] -= fc * n
    _vs[to] += tc * n
    return True, _vs


_, vs = step(vs, 2, 0, all=True)
_, vs = step(vs, 2, 1, all=True)
_, vs = step(vs, 1, 0, all=True)

mem = set()


def rec(state):
    t_state = tuple(state)
    if t_state in mem:
        return
    mem.add(t_state)
    flag, opt0 = step(state, 0, 1)
    if flag:
        rec(opt0)
    flag, opt1 = step(state, 0, 2)
    if flag:
        rec(opt1)
    flag, opt2 = step(state, 1, 2)
    if flag:
        rec(opt2)


rec(vs)


# print(mem)
print(len(mem))
