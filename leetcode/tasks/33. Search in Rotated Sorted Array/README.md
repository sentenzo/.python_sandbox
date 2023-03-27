# 33. Search in Rotated Sorted Array

[link to LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/) (<span style="color:orange">medium</span>)

## Description
There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index `3` and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the rotation and an integer `target`, return _the index of_ `target` _if it is in_ `nums`_, or_ `-1` _if it is not in_ `nums`.

You must write an algorithm with `O(log n)` runtime complexity.
## Constraints
-   `1 <= nums.length <= 5000`
-   `-10^4 <= nums[i] <= 10^4`
-   All values of `nums` are **unique**.
-   `nums` is guaranteed to be rotated at some pivot.
-   `-10^4 <= target <= 10^4`

## Examples
### Example 1:
**Input:** `nums = [4,5,6,7,0,1,2]`, `target = 0`
**Output:** `4`

### Example 2:
**Input:** `nums = [4,5,6,7,0,1,2]`, `target = 3`
**Output:** `-1`
## Abstract (TL;DR)
B-search twice.
## Thoughts
It's similar to [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/):
### Solution 1 (b-search*2)
```python
class Solution:
    def get_r_pivot(self, xs: List[int]) -> int:
        # return xs.index(min(xs))
        a, b = -1, len(xs)
        while b - a > 1:
            m = (a + b) // 2
            if xs[m]  > xs[a]:
                a = m
            elif xs[m] < xs[a]:
                b = m
            else:
                return m
        return b
    
    def b_search(self, xs, t) -> int:
        a, b = -1, len(xs)
        while b - a > 1:
            m = (a + b) // 2
            if xs[m] < t:
                a = m
            elif xs[m] > t:
                b = m
            else:
                return m
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        r = self.get_r_pivot(nums)
        print(r)
        nums = nums[r:] + nums[:r]
        ans = self.b_search(nums, target)
        if ans == -1:
            return -1
        else:
            return (r + self.b_search(nums, target)) % len(nums)
```
