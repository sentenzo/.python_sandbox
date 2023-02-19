# 21. Merge Two Sorted Lists

[link to LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/) (<span style="color:green">easy</span>)



## Description
Merge two sorted linked lists and return it as a **sorted** list. The list should be made by splicing together the nodes of the first two lists.
## Constraints
-   The number of nodes in both lists is in the range `[0, 50]`.
-   `-100 <= Node.val <= 100`
-   Both `l1` and `l2` are sorted in **non-decreasing** order.
## Examples
### Example 1:
**Input:** l1 = [1,2,4], l2 = [1,3,4]

**Output:** [1,1,2,3,4,4]

### Example 2:
**Input:** l1 = [], l2 = []

**Output:** []

### Example 3:
**Input:** l1 = [], l2 = [0]

**Output:** [0]

## Thoughts

### Solution 1 
The solution I've done months ago:
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode()
        rr = r
        while True:
            if (l1 and l2 and l1.val > l2.val) 
			or (not l1 and l2):
                rr.next = l2
                l2 = l2.next
            elif l1:
                rr.next = l1
                l1 = l1.next
            else:
                break
            rr = rr.next
        return r.next
```

### Solution 2
The solution I've done just now, trying to pay attention to not allocate additional memory. And it's an awful overly complicated mess 😭
```python
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not (l1 and l2):
            return l1 or l2
        pre = cur = ListNode()
        def nxt(l):
            if l:
                node = l
                l = l.next
                node.next = None
                return node, l
            else:
                return None, None

        n1, l1 = nxt(l1)
        n2, l2 = nxt(l2)
        while True:
            if not (n1 or n2):
                break
            elif n1 and not n2:
                cur.next = n1
                cur.next.next = l1
                break
            elif not n1 and n2:
                cur.next = n2
                cur.next.next = l2
                break
            else:
                if n1.val < n2.val:
                    cur.next = n1
                    n1, l1 = nxt(l1)
                else:
                    cur.next = n2
                    n2, l2 = nxt(l2)
                cur = cur.next
        
        return pre.next
```
It even works slightly faster and takes more memory than the previous approach.

#### UPD
```python
class Solution:
    def mergeTwoLists(self, l1, l2) -> Optional[ListNode]:
        head = tail = ListNode()
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 or l2
        
        return head.next
```

### Solution 3 (rec) ([**stolen**](https://leetcode.com/problems/merge-two-sorted-lists/discuss/9771/Simple-5-lines-Python))
```python
def mergeTwoLists(self, a, b):
    if not a or b and a.val > b.val:
        a, b = b, a
    if a:
        a.next = self.mergeTwoLists(a.next, b)
    return a
```
The other version:
```python
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
```

`if a and b:` - both `a` and `b` are not empty lists.
If any of them is empty, it will `return a or b` (the non-emptiest of two).

`if a.val > b.val: a, b = b, a` - we want `a` to be the smallest.

`a.next = self.mergeTwoLists(a.next, b)` - it has two parts: 
- `a_next = self.mergeTwoLists(a.next, b)` - we recursively build the tail of the list
- `a.next = a_next` - we join the tail to the head

`return a or b` - the order is important. `a` is the head on the current stage, and it would be returned instate of `b` (which is now located somewhere in the tail of `a`).