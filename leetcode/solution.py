from collections import *
from typing import *
from functools import *
from heapq import *

from lc.singly_linked_list import *
from lc.binary_tree import *


class Solution:
    """
    https://leetcode.com/problems/increasing-order-search-tree/
    """
    def increasingBST(self, root: TreeNode) -> TreeNode:
        que = [root]
        ans = pos = None
        while que:
            cur = que.pop()
            if isinstance(cur, tuple):
                if ans:
                    pos.right = cur[0]
                    pos = pos.right
                    pos.left = None
                else:
                    ans = pos = cur[0]
                    pos.left = None
            else:
                if cur.right:
                    que.append(cur.right)
                que.append((cur,))
                if cur.left:
                    que.append(cur.left)
        return ans

inp = stringToTreeNode("[5,3,6,2,4,null,8,1,null,null,null,7,9]")
prettyPrintTree(inp)

ans = Solution().increasingBST(
    inp
)

prettyPrintTree(ans)
