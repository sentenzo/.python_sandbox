"""
A dummy
"""

DBG = True

INP = """
4 6
1 3 0
3 4 0
3 4 1
1 2 1
2 3 1
2 4 0
""".strip().split(
    "\n"
)


def _input():
    if DBG:
        return INP.pop(0)
    else:
        return input()


#################

from collections import defaultdict, deque

n, m = map(int, _input().split())

graph0 = defaultdict(set)
graph1 = defaultdict(set)

for _ in range(m):
    u, v, t = map(int, _input().split())
    graph = [graph0, graph1][t]
    graph[u].add(v)
    # print(_input())

print(graph0)
print(graph1)

ans = []
for i in range(1, n):
    opt0 = graph0[i]
    opt1 = graph1[i]
    if (i + 1) not in opt0:
        ans.append("1")
        ans.append("0" * n - i)
        print(-1)
        print("".join(ans))
        break
    if (i + 1) not in opt0:
        ans.append("0")
        ans.append("0" * n - i)
        print(-1)
        print("".join(ans))
        break

    ...


que = deque([1])
