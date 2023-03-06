# 18. 4Sum

[link to LeetCode](https://leetcode.com/problems/4sum/) (<span style="color:orange">medium</span>)

## Description
Given an array `nums` of `n` integers, return _an array of all the **unique** quadruplets_ `[nums[a], nums[b], nums[c], nums[d]]` such that:

-   `0 <= a, b, c, d < n`
-   `a`, `b`, `c`, and `d` are **distinct**.
-   `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in **any order**.

## Constraints
-   `1 <= nums.length <= 200`
-   `-10^9 <= nums[i] <= 10^9`
-   `-10^9 <= target <= 10^9`

## Examples
### Example 1:

**Input:** `nums = [1,0,-1,0,-2,2]`, `target = 0`

**Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`

### Example 2:

**Input:** `nums = [2,2,2,2,2]`, `target = 8`

**Output:** `[[2,2,2,2]]`

## Abstract (TL;DR)
Sort the `nums`. Any solution would take more than $O(N\ log\ N)$, so we loose nothing.

Peak 1st and 2nd elements with brute force.

For the last two elements you can apply either the Two Pointers approach (like in [2Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)), or the Dictionary approach (like in [Two Sum](https://leetcode.com/problems/two-sum/)).

The latter one works on the unsorted data too, but sorting allows doing some tricky optimizations.

## Thoughts
The `nums.length` constraint is very short.
### Solution 1 (naive brute-force) (<span style="color:red">Time Limit Exceeded</span>)
... but `200**4` will be $\large 1.6\cdot 10^9$, and it's too big anyways.
> even if each iteration would take just one [L1 cache reference](https://github.com/donnemartin/system-design-primer/blob/master/README.md#latency-numbers-every-programmer-should-know), it would already take: $1.6\cdot 10^9\cdot0.5 \cdot 10^{-9}=$<span style="color:red">**$0.8$ seconds**</span> (NOT mili or micro).
```python
from itertools import combinations
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = set()
        for c in combinations(nums, 4):
            if sum(c) == target:
                r.add(tuple(sorted(c)))
        return list(r)
```

#### Score
| Runtime (ms) | - % | O               | Memory (Mb) | - % | O             |
| ------------ | --- | --------------- | ----------- | --- | ------------- |
| \>3000       | TLE | $\large O(N^4)$ | -           | TLE | $\large O(1)$ |



### Solution 2 (N^3 diff dict)
```python
class Solution:
    def fourSum(self, ns: List[int], target: int) -> List[List[int]]:
        n = len(ns)
        if n < 4: return []
        
        ns.sort()
        d = defaultdict(list)
        for i, v in enumerate(ns):
            d[v].append(i)
              
        ans = []
        
        for a in range(n-3):
            va = ns[a]
            for b in range(a+1, n-2):
                vb = ns[b]
                for c in range(b+1, n-1):
                    vc = ns[c]
                    vd = target - va - vb - vc
                    if vd in d and d[vd][-1] > c:
                        ans0 = [va,vb,vc,vd]
                        if not ans0 in ans:
                            ans.append(ans0)
        return ans
```

`ans = []` can be replaced with `ans = set()` if we think too many answers will be found.

#### Score
| Runtime (ms) | - %    | O               | Memory (Mb) | - %  | O             |
| ------------ | ------ | --------------- | ----------- | ---- | ------------- |
| 748          | 61.89% | $\large O(N^3)$ | -           | 14.2 | $\large O(N)$ |

It's a trade-off $\large O(N^4|1)$ to $\large O(N^3|N)$

### Solution 2 (N^2 comb) (<span style="color:red">Time Limit Exceeded</span>)

I've spent some time (~1 hour) on this approach. I had an idea that by having a (Cartesian) product of $\large nums \times nums$ we'll be having a $\large O(N^2|N^2)$ trade-off. But I got TLE, and [this guy says](https://leetcode.com/problems/4sum/discuss/8565/Lower-bound-n3) it's impossible to have it faster than in $\large O(N^3)$. 

```python
class Solution:
    def fourSum(self, xs: List[int], target: int) -> List[List[int]]:
        n = len(xs)
        if n < 4: return []
        
        comb = {}
        for i, a in enumerate(xs):
            for j, b in enumerate(xs):
                if i != j:
                    val = sorted([i, j])
                    val = tuple(val)
                    if a + b in comb:
                        comb[a + b].add(val)
                    else:
                        comb[a + b] = {val}
        
        diff = {}
        for k in comb:
            if target - k in diff:
                diff[target - k] |= comb[k]
            else:
                diff[target - k] = set(comb[k])

        ans = set()
        for k in comb:
            if k in diff:
                for c in comb[k]:
                    for d in diff[k]:
                        a = set(c + d)
                        if len(a) == 4:
                            a = list(a)
                            v = sorted(xs[i] for i in a)
                            ans.add(tuple(v))
                            
        return ans
```
I think the additional complexity is hidden in my inner `for * for` cycle. In come cases it would take quite a time.

### Solution 3 (N^3 two pointers)
Using the approach from [2Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) task (the input is sorted).
```python
class Solution:
    def fourSum(self, xs: List[int], target: int) -> List[List[int]]:
        n = len(xs)
        if n < 4: return []
        
        xs.sort()
        ans = set()
        for i in range(0, n - 3):
            for j in range(i + 1, n - 2):
                t = target - xs[i] - xs[j]
                a, b = j + 1, n - 1
                while True:
                    if a >= b:
                        break
                    else:
                        v = xs[a] + xs[b]
                        if v > t:
                            b -= 1
                        elif v < t:
                            a += 1
                        else:
                            ans.add((xs[i], xs[j], xs[a], xs[b]))
                            b -= 1
                            a += 1
        return ans
```

#### Score
| Runtime (ms) | - %    | O               | Memory (Mb) | - %  | O             |
| ------------ | ------ | --------------- | ----------- | ---- | ------------- |
| 1172         | 30.50% | $\large O(N^3)$ | 77.43       | 14.2 | $\large O(N)$ |

This result can be improved significantly with just one check: ^a2e886
```python
###################################...
        xs.sort()
        ans = set()
        for i in range(0, n - 3):
			
################################### VVVVV
            if i > 0 and xs[i] == xs[i-1]:
                continue
            if xs[i] + xs[i+1] + xs[i+2] + xs[i+3] > target:
                break
            if xs[i] + xs[n-3] + xs[n-2] + xs[n-1] < target:
                continue
################################### ^^^^^

            for j in range(i + 1, n - 2):
                t = target - xs[i] - xs[j]
                a, b = j + 1, n - 1
###################################...
```


#### Score
| Runtime (ms) | - %    | O               | Memory (Mb) | - %  | O             |
| ------------ | ------ | --------------- | ----------- | ---- | ------------- |
| 136          | 75.34% | $\large O(N^3)$ | 55.43       | 14.4 | $\large O(N)$ |

Probably, it's only related with the specifics of the tests on the LeetCode platform.
