# 23. Merge k Sorted Lists

[link to LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/) (<span style="color:red">hard</span>)

## Description
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Constraints
-   `k == lists.length`
-   `0 <= k <= 10^4`
-   `0 <= lists[i].length <= 500`
-   `-10^4 <= lists[i][j] <= 10^4`
-   `lists[i]` is sorted in **ascending order**.
-   The sum of `lists[i].length` won't exceed `10^4`.
## Examples
### Example 1:

**Input:** `lists = [[1,4,5],[1,3,4],[2,6]]`
**Output:** `[1,1,2,3,4,4,5,6]`
**Explanation:** The linked-lists are:
``` python
[
  1->4->5,
  1->3->4,
  2->6
]
```
merging them into one sorted list:
`1->1->2->3->4->4->5->6`

### Example 2:

**Input:** `lists = []`
**Output:** `[]`

### Example 3:

**Input:** lists = `[[]]`
**Output:** `[]`

## Thoughts
The first idea is to generalize the approach for the [LeetCode 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) task.
Though now I think it was quite crude. I didn't pay enough attention to the constraints. I thought `len(lists)` would be less than `len(lists[i])`.
It almost failed with <span style="color:red">Time Limit Exceeded</span>. Here it is:
### Solution 1 (crude generalize)
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def min_ind_val(arr: List[int]) -> Tuple[int, int]:
            val = float("inf")
            ind = -1
            for i in range(len(arr)):
                if arr[i] < val:
                    val = arr[i]
                    ind = i
            return (ind, val)
        
        pre = cur = ListNode()
        
        # [[1,4,5],[1,3,4],[2,6]]
        lists = [l for l in lists if l]
        while lists:           
            chunk = [l.val for l in lists] # [6]
            while True:
                ind, val = min_ind_val(chunk) # 0, 6
                cur.next = ListNode(val) 
				# * -> 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
                cur = cur.next
                # print(ind)
                lists[ind] = lists[ind].next # [[]]
                if lists[ind]:
                    chunk[ind] = lists[ind].val # [5 4 6]
                else:
                    break           
            lists = [l for l in lists if l]
        
        return pre.next
```

#### Score
| Runtime (ms) | - %   | Memory (Mb) | - %    |
| ------------ | ----- | ----------- | ------ |
| 7008         | 5.01% | 18.7        | 15.45% |

#### Complexity Analysis
`K` - `len(lists)`
`M` - `avg(len(l) for l in lists)`
##### Time:
`min_ind_val(arr)` takes $\large O(K)$
`while True:` - inner `while` cycle repeats $\large K\times M$ times.

So the complexity would be $\large O(K^2M)$

### Solution 2 (take by two)
If we already have the function to merge two lists, we can easily generalize it:
```
(A B) (C D) (E F) (G H)
(AB CD) (EF GH)
(ABCD EFGH)
 ABCDEFGH
```
So, I've taken the solution from [LeetCode 21](https://leetcode.com/problems/merge-two-sorted-lists/) I've done some time ago and modified it. Even though it uses additional memory, it works very fast.
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode()
        rr = r
        while True:
            if l1 and l2 and l1.val > l2.val or not l1 and l2:
                rr.next = l2
                l2 = l2.next
            elif l1:
                rr.next = l1
                l1 = l1.next
            else:
                break
            rr = rr.next
        return r.next
        
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        while len(lists) > 1:
            nxt_lists = []
            for i in range(1, len(lists), 2):
                nxt_lists.append(self.mergeTwoLists(lists[i-1], lists[i]))
            if len(lists) % 2:
                nxt_lists.append(lists[-1])
            lists = nxt_lists
        return lists[0] if lists else None
```
The $\large O(1)$ memory `mergeTwoLists` is also appropriate, but it works slightly slower and it's a lot more complicated to implement.

#### Score
| Runtime (ms) | - %    | Memory (Mb) | - %    |
| ------------ | ------ | ----------- | ------ |
| 120          | 45.41% | 17.8        | 66.57% |
