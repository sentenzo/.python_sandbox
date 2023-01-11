from collections import *
from typing import *
from functools import *
from heapq import *

from singly_linked_list import *

from math import factorial

class Solution:
    """
    https://leetcode.com/problems/remove-nodes-from-linked-list/
    """
    def removeNodes(self, head: Optional[ListNode], mx = float("-inf")) -> Optional[ListNode]:
        
        lst = []
        cur = head
        while cur:
            v = cur.val
            while lst and lst[-1] < v:
                lst.pop()
            lst.append(v)
            cur = cur.next
        
        root = ListNode(None)
        cur = root
        for x in lst:
            cur.next = ListNode(x)
            cur = cur.next
        return root.next


ans = Solution().removeNodes(
    stringToListNode("[5,2,13,3,8]")
)

prettyPrintLinkedList(ans)
