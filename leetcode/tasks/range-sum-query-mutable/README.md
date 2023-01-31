# LeetCode 307. Range Sum Query - Mutable

[link to LeetCode](https://leetcode.com/problems/range-sum-query-mutable/) (<span style="color:orange">medium</span>)

## Description
We are given a potentially big array of integer numbers (`nums`). Our program should be capable of efficiently perform a flow of commands of two kinds: 
1. Given an index (`index`) and a number (`val`) change the value at the `index` to `val`
2. Given two indexes `left` and `right` calculate sum of elements between them

## Constraints
-   `1 <= nums.length <= 3 * 10^4`
-   `-100 <= nums[i] <= 100`
-   `0 <= index < nums.length`
-   `-100 <= val <= 100`
-   `0 <= left <= right < nums.length`
-   At most `3 * 10^4` calls will be made to `update` and `sumRange`.

## Examples

```python
obj = NumArray([14, -3, 0, -9])
print(obj.sumRange(2, 3)) # sum([0, -9]) -9
obj.update(2, 1) # [14, -3, 1, -9]
print(obj.sumRange(0, 3)) # sum([14, -3, 1, -9]) == 3
```

## Abstract (TL;DR)
Use the [Segment Tree](https://en.wikipedia.org/wiki/Segment_tree) data structure.

## Thoughts
I did the naive approach just to get started and to be sure I understood the task correctly. Here it is:

### Solution 1 (<span style="color:red">Time Limit Exceeded</span>)
```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.xs = nums

    def update(self, index: int, val: int) -> None:
        self.xs[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.xs[left:right+1])
```
The bottleneck is the size of the array (and the fact that it's mutable)

---

My first idea was to use running sums somehow, but it was soon discarded due to the mutability of the array. If `nums[i]` is changed, then we should recalculate all the running sums from `j` up to `len(nums) - 1`. And the values in `nums` are actually changing a lot. In one test case it was more then `10_000` `update` operations.

---
The next approach: hashing. I didn't gain any code out of it, but the line of thoughts was:

How can I reuse once calculated ranges? Maybe if we've had `obj.sumRange(2060, 2200)` and now we are to do `obj.sumRange(0, 3000)` and where was no changes inside `2060 .. 2200`, so we can reuse the result of the previous calculations like this:
 ```python
 obj.sumRange(0, 3000): 
   obj.sumRange(2060, 2200) 
   + sum(nums[0:2060])
   + sum(nums[2201:3000])
 ```

But what to do with updates? If we've changed the value `nums[i]`, should we change all the hashed sums where it was involved. Well, the main question is how to find all such sums fast enough. Like what if we have:
```python
hash = {(430, 1562): 25
      , (0, 36782): 825300
	  , (70001, 70002): -8
	  , ...}
# ...
obj.update(12012, 35) # nums[12012]: 37 -> 35
```
So, knowing the index (`index = 12012`) and the difference between old and new value (`val - nums[index] == 35-37 == -2`), how can we efficiently modify `hash` to preserve its consistency?

---
So I gave up and went to the solution section to embrace and accept my negligibility 😔😞

There's more than one way to solving this task, described in solutions. I've chosen a [[Data Structure. Segment Tree|Segment Tree]] (Дерево отрезков) approach. And yes, looks like this is a data-structure task. The only thing one should do to successfully finish it is successfully apply the appropriate data structure. Can't say anything good about my implementation though. (What? I had a short of time.)

## Solution 2 (Segment Tree)

```python
class NumArray:

    def __init__(self, nums: List[int]):
        xs = nums
        self.xs = xs
        l = len(nums)
        l2 = 1 << len(bin(l - 1)) - 2
        xs += [0] * (l2 - l)
        xss = [xs]
        nxt = lambda xs: list(map(sum, zip(xs[::2], xs[1::2])))
        while True:
            xss.append(nxt(xss[-1]))
            if len(xss[-1]) == 1:
                break
        self.xss = xss
            
# """       *      *
# [1, 3, 2, 3, 1, -4, 3, 2, 8, -12, 0, 0, 0, 0, 0, 0]
# [  4,    5,    -3,    5,    -4,     0,    0,    0]
# [      9,           2,          -4,          0]
# [            11,                      -4]
# [                         7]
# 3 - 5 -9 -11
# -4 - -3 - 2 - 11
# """

    def update(self, index: int, val: int) -> None:
        i = index
        diff = val - self.xss[0][i]
        for z in range(len(self.xss)):
            self.xss[z][i] += diff
            i //= 2
        
    def running_sum(self, i):
        if i < 0:
            return 0
        b = bin(i)[2:] # 
        b = "0" * (len(self.xss) - len(b) - 1) + b
        z = len(self.xss) - 1
        i = 0
        ans = self.xss[z][i]
        for c in b:
            z -= 1
            if c == "0":
                i = i * 2
                ans -= self.xss[z][i + 1]
            else:
                i = i * 2 + 1
        return ans

    def sumRange(self, left: int, right: int) -> int:
        return self.running_sum(right) - self.running_sum(left - 1)
```
What I **don't** like here:
- the way how I count the ranges: running sums were easier to implement, but supposedly not the best choice for speed
- (marginal) it can be done with lazy calculations

Anyways, this solution has a good score: 
##### Runtime:
1596ms - 82.24%  
##### Memory:
32Mb - 45.74%

## Solution 3 (The Real Segment Tree)

Somehow I got capable to implement it in a more general way - it is not relied on the inverse operation (for the `sum` aggregator it would be the `-` operation).

But it works 2 times slower.

```python
from math import log2, ceil
class NumArray:

    def __init__(self, nums: List[int]):
        self.lvls = []
        n = 2 ** ceil( log2(len(nums)) )
        
        self.lvls.append(nums[:])
        for _ in range(n - len(nums)):
            self.lvls[0].append(0)
            
        while True:
            prv = self.lvls[-1]
            if len(prv) == 1:
                break
            lvl = []
            for i in range(0, len(prv) - 1, 2):
                lvl.append(prv[i] + prv[i + 1])
            self.lvls.append(lvl)

    def update(self, index: int, val: int) -> None:
        dif = val - self.lvls[0][index]
        for lvl in self.lvls:
            lvl[index] += dif
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        def rec(k=len(self.lvls) - 1, i=0, a=left, b=right+1):
            if a == b:
                return 0
            sz = 2 ** k
            l, r = (sz * i, sz * (i + 1))
            if (a, b) == (l, r):
                return self.lvls[k][i]
            else:
                m = sz * i + sz // 2
                if b < m:
                    return rec(k - 1, i * 2, a, b)
                elif m <= a:
                    return rec(k - 1, i * 2 + 1, a, b)
                else:
                    return rec(k - 1, i * 2, a, m) + rec(k - 1, i * 2 + 1, m, b)
        return rec()
```

##### Runtime:
3384 ms - 20.77%
##### Memory:
31.3 MB - 80.19%
