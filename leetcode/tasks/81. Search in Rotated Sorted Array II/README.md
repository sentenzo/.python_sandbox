# Leetcode 81. Search in Rotated Sorted Array II

[link to LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/) (<span style="color:orange">medium</span>)

... and I've spent ~3 hours on solving it.

## Description
There is an integer array `nums` sorted in non-decreasing order (not necessarily with **distinct** values).

Before being passed to your function, `nums` is **rotated** at an unknown pivot index `k` (`0 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (**0-indexed**). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated at pivot index `5` and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` **after** the rotation and an integer `target`, return `true` _if_ `target` _is in_ `nums`_, or_ `false` _if it is not in_ `nums`_._

You must decrease the overall operation steps as much as possible.

## Constraints
-   `1 <= nums.length <= 5000`
-   `-10^4 <= nums[i] <= 10^4`
-   `nums` is guaranteed to be rotated at some pivot.
-   `-10^4 <= target <= 10^4`

## Examples
```python
nums = [2,5,6,0,0,1,2]
target = 0
>> True

nums = [2,5,6,0,0,1,2]
target = 3
>> False

nums = [1,3]
target = 1
>> True

nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
>> True

nums = [1,3,5]
target = 1
>> True

nums = [2,2,2,0,2,2]
target = 0
>> True

nums = [1]
target = 1
>> True

nums = [0,0,1,1,2,0]  
target = 2
>> True
```

## Abstract (TL;DR)
Binary search on un-rotated array. B-search part is easy. But Gods help you to finish up the search of the rotation pivot in less then half an hour.

## Thoughts
I wont to separate in in two steps:
1. Finding the rotation pivot (`p = p_rot(...)`)
2. `nums = nums[p:] + nums[:p]`
3. Binary search on the sorted array

Practically it's the same as [Leetcode 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/). The important detail is: there can be repeated elements in `nums`.

### Solution 1 (double b-search)
```python
class Solution:
    def p_rot(self, xs: List[int]) -> int:
        a, b = 0, len(xs) - 1
        while xs[a] == xs[b] and a < b:
            a += 1
        if xs[a] < xs[b]:
            return a
        while b - a > 1:
            m = (a + b) // 2
            if xs[m] < xs[a]:
                b = m
            else:
                a = m
        return b
    
    def b_search(self, xs: List[int], t: int) -> int:
        a, b = -1, len(xs)
        while b - a > 1:
            m = (a + b) // 2
            if xs[m] == t:
                return m
            elif xs[m] < t:
                a = m
            else:
                b = m
        return -1
    
    def search(self, nums: List[int], target: int) -> bool:
        r = self.p_rot(nums)
        nums = nums[r:] + nums[:r]
        i = self.b_search(nums, target)
        return i > -1
```

`b_search` has nothing to worry about since we don't need to return the index of the element to insert.

`p_rot` - deserves a lot more attention.

#### The search of the rotation pivot (`def p_rot(...):`)

##### The `while xs[a] == xs[b] and a < b:` part

At first we should understand where we are located. If `xs` is of size `len(xs) == 10_000_000_000`, starts with `[6,6,6,6, ...` and ends with `..., 6,6,6]`, we can't say if it's `set(xs) == {6}`, or maybe it is `[...6,6,7,6, ...]`, or `[...6,6,3,6, ...]`. Unfortunately, the only way to find out is to check each element till we find the one which is not `6`.

So, we are moving `a` to the right.

##### The `if xs[a] < xs[b]:` part

This is an important check. It happens in some border cases.

If `xs[a] < xs[b]`, and `set(xs[:a]) == {xs[b:]}`, the only explanation is: `a` is the pivot. Congratulations! We found it.

##### The `while b - a > 1:` part
It's a binary search. We are willing to get the state where:
- `b - a == 1`
- `xs[a] > xs[b]` (so the pivot is between them)

This section breaks if there's no pivot between `a` and `b` at the first iteration.  That's why we needed all that checks in the beginning.

### Solution 2 (dumb as hack)
```python
class Solution:    
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums
```
It works **FASTER** than the previous one 🤦‍♂️.


