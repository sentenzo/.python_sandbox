# Leetcode 1. Two Sum

[link to LeetCode](https://leetcode.com/problems/two-sum/) (<span style="color:green">easy</span>)

This was the first task in LeetCode I've ever done, many years ago (on C# in $\large O(N^2)$ time 😬) 

## Description
Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.
## Constraints
-   `2 <= nums.length <= 104`
-   `-109 <= nums[i] <= 109`
-   `-109 <= target <= 109`
-   **Only one valid answer exists.**
## Examples
### Example:

**Input:** `nums = [2,7,11,15]`, `target = 9`

**Output:** `[0,1]`

**Output:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

## Abstract (TL;DR)
Memorize the indexes `i` of the values `x` into dict by key `target - x`.
## Thoughts

Retried it just now:
### Solution 1 (dict of diffs)
```python
class Solution:
    def twoSum(self, xs: List[int], t: int) -> List[int]:
        diffs = {}
        for i, x in enumerate(xs):
			val = diffs.setdefault(t - x, [])
			val += [i]
            diffs[t - x] = val
        
        for i, x in enumerate(xs):
            if x in diffs:
                for ii in diffs[x]:
                    if i != ii:
                        return [i, ii]
```

#### Improved:
Why to keep the list of indexes if we can only keep the last ones?
```python
class Solution:
    def twoSum(self, xs: List[int], t: int) -> List[int]:
        diffs = {}
        for i, x in enumerate(xs):
            if x in diffs:
                return [i, diffs[x]]
            diffs[t - x] = i
```

Time: $\large O(N)$
Memory: $\large O(N)$