# 56. Merge Intervals

[link to LeetCode](https://leetcode.com/problems/merge-intervals/) (<span style="color:orange">medium</span>)

## Description
Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input_.

## Constraints
-   `1 <= intervals.length <= 10^4`
-   `intervals[i].length == 2`
-   `0 <= starti <= endi <= 10^4`
## Examples
| Input                                         | Output                   |
| --------------------------------------------- | ------------------------ |
| `[[1,3],[2,6],[8,10],[15,18]]`                | `[[1,6],[8,10],[15,18]]` |
| `[[1,4],[4,5]]`                               | `[[1,5]]`                |
| `[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]` | `[[1,3],[4,7]]`          |
## Abstract (TL;DR)
Sort by left border. Join all of them in one walk-thru.
## Thoughts
I wanted to start from something brute.
### Solution 1 (in-memory timeline)
In this solution I create an array of the size of the max `end_i` multiplied by two. This is how the concept works:
```python
[1, 4]
-> [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, ...
#   0  0  1  1  2  2  3  3  4  4  5  5  6  6
#         xxxxxxxxxxxxxxxxxxx
[2, 2], [3, 3], [3, 4], [4, 4], [5, 5]
-> [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, ...
#   0  0  1  1  2  2  3  3  4  4  5  5  6  6
#               x     xxxxxxx     x
```
And this is the code:
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mn = max(intervals, key=lambda e: e[1])[1]
        mem = [0] * (2*(mn))
        
        for interval in intervals:
            a, b = interval
            a *= 2
            b = 2*(b+ 1) - 1
            mem[a:b] = [1]*(b-a)
        
        ans = []
        fl = True
        a = None
        for i, x in enumerate(mem):
            if x:
                if fl:
                    fl = False
                    a = i//2
            else:
                if not fl:
                    fl = True
                    ans.append([a, (i)//2])
                    a = None
        if a != None:
            ans.append([a, mn])        
        return ans
```
Surprisingly, no TLE.
#### Score
| Runtime (ms) | - %     | O             | Memory (Mb) | - %     | O             |
| ------------ | ------- | ------------- | ----------- | ------- | ------------- |
| 84           | 75.80 % | $\large O(M)$ | 16.1        | 55.17 % | $\large O(M)$ |
> \* $\large M = max(end) -min(start)$


### Solution 2 (sort)
The only thing why I got to this approach is the fact that this task was with the **Sort** tag. A big hint.

We can sort the intervals by first element. After that we need to only check the neighboring intervals if they intersect.

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda e: e[0])
        ans = []
        p, q = intervals[0]
        for interval in intervals[1:]:
            a, b = interval
            if p <= a <= q:
                if b > q:
                    q = b
            else:
                ans.append([p, q])
                p, q = a, b
        ans.append([p, q])
        return ans
```



#### Score
| Runtime (ms) | - %     | O                         | Memory (Mb) | - %     | O   |
| ------------ | ------- | ------------------------- | ----------- | ------- | --- |
| 72           | 99.49 % | $\large O(N\cdot log(N))$ | 16.1        | 55.17 % | ?   |


