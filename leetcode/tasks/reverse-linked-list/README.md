# LeetCode 206. Reverse Linked List

[link to LeetCode](https://leetcode.com/problems/reverse-linked-list/ ) (<span style="color:green">easy</span>)

## Description
Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?
## Constraints
-   The number of nodes in the list is the range `[0, 5000]`.
-   `-5000 <= Node.val <= 5000`
## Examples
**Input:** `head = [1,2,3,4,5]`

**Output:** `[5,4,3,2,1]`
## Thoughts

### Solution 1 (two pointers)
The first idea came into my thoughts:
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        fst = None
        snd = head
        while snd:
            tmp = fst
            fst = snd
            snd = snd.next
            fst.next = tmp
        return fst
```
You can shrink it up to this:
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        fst, snd = None, head
        while snd:
            snd.next, fst, snd = fst, snd, snd.next
        return fst
```

### Solution 2 (my clumsy recursion)
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def rec(lst = head):
            if lst == None or lst.next == None:
                return lst, lst
            else:
                rev0, rev1 = rec(lst.next)
                rev1.next = lst
                lst.next = None
                return rev0, lst
        return rec()[0]
```

### Solution 3 (recursion) (**stolen**)
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail
```
How it works:
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        def rec(node):
            if not (node and node.next):
                return node
            tail = rec(node.next)
            node.next.next = node
			# node.next = None
            return tail
        ans = rec(head)
        head.next = None
        return ans
```

#### My late implementation
(I think this one is more readable)
```python
class Solution:
    def reverseList(self, head: ListNode, prv = None) -> ListNode:
        if not head:
            return prv
        else:
            ans = self.reverseList(head.next, head)
            head.next = prv
            return ans
```

### Solution 4 (naive array approach)
The thing is - it works **very fast**.
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        for i in range(1, len(nodes)):
            nodes[i].next = nodes[i-1]
        nodes[0].next = None
        return nodes[-1]
```