# Leetcode 11. Container With Most Water

[link to LeetCode](https://leetcode.com/problems/container-with-most-water/) (<span style="color:orange">medium</span>)

## Description
Given `n` non-negative integers `a1, a2, ..., an` , where each represents a point at coordinate `(i, ai)`. `n` vertical lines are drawn such that the two endpoints of the line `i` is at `(i, ai)` and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

## Constraints
-   `n == height.length`
-   `2 <= n <= 105`
-   `0 <= height[i] <= 104`
## Examples
![img1.png](img1.png)
**Input:** `height = [1,8,6,2,5,4,8,3,7]`

**Output:** `49`

**Explanation:** The above vertical lines are represented by array `[1,8,6,2,5,4,8,3,7]`. In this case, the max area of water (blue section) the container can contain is `49`.

## Abstract (TL;DR)
Start with `a = 0` and `b = n-1`. Move the lowest of them one step to the center. Repeat.
## Thoughts

### Solution 1 (two pointers)
#### Python minimalistic
```python
class Solution:
    def maxArea(self, hs: List[int]) -> int:
        a, b = 0, len(hs) - 1
        ans = 0
        while a < b:
            ans = max(ans, min(hs[a], hs[b]) * (b - a))
            if hs[a] < hs[b]:
                a += 1
            else:
                b -= 1
        return ans
```
**Runtime**: 784 ms - 21.65%

**Memory Usage**: 27.6 MB - 56.87%

#### Python optimized
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        a, b = 0, len(height) - 1
        s_max = (b - a) * min(height[a], height[b])
        while a < b:
            s_max = max(s_max, (b - a) * min(height[a], height[b]))
            if height[a] < height[b]:
                old_v = height[a]
                while height[a] <= old_v and a < b:
                    a += 1
            else:
                old_v = height[b]
                while height[b] <= old_v and a < b:
                    b -= 1
        return s_max
```
**Runtime**: 596 ms - 98.96%

**Memory Usage**: 27.2 MB - 87.30%

#### Java optimized
```java
class Solution {
    public int maxArea(int[] hs) {
        int a = 0;
        int b = hs.length - 1;
        int win_max = 0;
        
        while (a < b) {
            int win_val = (b - a) * Math.min(hs[a], hs[b]);
            win_max = Math.max(win_val, win_max);

            if (hs[a] < hs[b]) {
                int tmp = hs[a];
                while (hs[a] <= tmp && a < b) {
                    a += 1;
                }
            } else {
                int tmp = hs[b];
                while (hs[b] <= tmp && a < b) {
                    b -= 1;
                }
            }
        }
        return win_max;
    }
}
```
**Runtime**: 1 ms - 100.00%

**Memory Usage**: 52.8 MB - 48.51%