from collections import *
from typing import *
from functools import *
from heapq import *

from lc.singly_linked_list import *
from lc.binary_tree import *
from math import *


import sortedcontainers as sc


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        def rec(cur, prv):
            people = 0
            fuel = 0
            for nxt in graph[cur]:
                if nxt == prv:
                    continue
                p, f = rec(nxt, cur)
                people += p
                fuel += f
                fuel += ceil(p/seats)
            people += 1
            return (people, fuel)
            
        _, ans = rec(0, None)
        return ans


ans = Solution().minimumFuelCost(
    [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]],
    2,
)

print(ans)
