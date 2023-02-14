# 704. Binary Search

[link to LeetCode](https://leetcode.com/problems/binary-search/) (<span style="color:green">easy</span>)

## Description
Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## Constraints
-   `1 <= nums.length <= 10**4`
-   `-10**4 < nums[i], target < 10**4`
-   All the integers in `nums` are **unique**.
-   `nums` is sorted in ascending order.
## Examples
**Input:** `nums = [-1,0,3,5,9,12]`, `target = 9`

**Output:** `4`

**Explanation:** 9 exists in nums and its index is 4


## Thoughts

### Solution 1 (`while` cycle)
This is how I've solved it just now:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums)
        # m         v
        #   [-1,0,3,5,10,12,13]
        # a         ^
        # b            ^
        if nums[a] == target:
            return a
        while b - a > 1:
            m = (a + b) // 2
            if nums[m] < target:
                a = m
            elif nums[m] > target:
                b = m
            elif nums[m] == target:
                return m
            else:
                return -2
        return -1
```
Here I use half-intervals. `b` index is not included into check. Initially `b = len(nums)`, so it's out of range. Then it can change by taking the value of `m` (and `m` is checked for NOT being an answer). What am I trying to proclaim here: `b` is NEVER an answer.

If `b - a` becomes `1` at some point, that means the answer is ether `a` or `-1`. But we've already checked `a` on the previous steps (the `if` condition checks it for borderline cases when `len(nums) in [1,2]`). Thus we can be sure we should return `-1`.

`else: return -2` branch is optional. It only works if we got unusual input like  `NaN` in some languages.

Actually, I could use excluding intervals instate: `a = -1`, ` b = len(nums)`. It would relive me from the `if` check in the beginning.
### Solution 2 (rec)
This is how I've solved it 9 months ago:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(haystack, needle, start, end):
            if end - start == 0:
                return -1
            elif end - start == 1:
                return [-1, start][haystack[start] == needle]
            else:
                middle = (start + end) // 2
                if needle < haystack[middle]:
                    return bSearch(haystack, needle, start, middle)
                elif needle > haystack[middle]:
                    return bSearch(haystack, needle, middle, end)
                else:
                    return middle
        return bSearch(nums, target, 0, len(nums))
```

And this one is a fresh implementation:
```python
class Solution:
    def search(self, xs: List[int], t: int) -> int:
        if not xs:
            return -1
        
        def rec(a = 0, b = len(xs) - 1):
            if b - a < 2:
                if xs[a] == t:
                    return a
                elif xs[b] == t:
                    return b
                else:
                    return -1
            m = (a + b) // 2
            if xs[m] == t:
                return m
            elif xs[m] < t:
                return rec(m + 1, b)
            else:
                return rec(a, m - 1)
        
        return rec()
```