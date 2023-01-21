# Leetcode 239. Sliding Window Maximum


[link to LeetCode](https://leetcode.com/problems/sliding-window-maximum/) (<span style="color:red">hard</span>)

## Description
You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

Return _the max sliding window_.
## Constraints
-   `1 <= nums.length <= 10^5`
-   `-10^4 <= nums[i] <= 10^4`
-   `1 <= k <= nums.length`
## Examples

**Input:** `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
**Output:** `[3,3,5,5,6,7]`
**Explanation:** 

| Window position              | Max     |
| ---------------------------- | ------- |
| `[1  3  -1] -3  5  3  6  7 ` | **`3`** |
| ` 1 [3  -1  -3] 5  3  6  7 ` | **`3`** |
| ` 1  3 [-1  -3  5] 3  6  7 ` | **`5`** |
| ` 1  3  -1 [-3  5  3] 6  7`  | **`5`** |
| ` 1  3  -1  -3 [5  3  6] 7`  | **`6`** |
| ` 1  3  -1  -3  5 [3  6  7]` | **`7`** |

## Abstract (TL;DR)

Use `heap` - $\large O(Nlog(N))$ 
or `deque` ([monotonic queue](https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem)) - $\large O(N)$.

## Thoughts
I've decided to use heap.
### Solution 1 (heap)
```python
class Solution:
    def maxSlidingWindow(self, xs: List[int], k: int) -> List[int]:
        win = [-x for x in xs[:k]]
        heapify(win)
        pas = Counter()
        ans = []
        for i in range(k, len(xs) + 1):
            while True:
                a = -win[0]
                if pas[a] > 0:
                    pas[a] -= 1
                    heappop(win)
                else:
                    ans.append(a)
                    break
            if i == len(xs):
                break
            heappush(win, -xs[i])
            pas[xs[i - k]] += 1
        return ans
```
`win` - the sliding window. We reform it into a heap. `*-1` cause Python is not into max-heaps.
`pas` - the `Counter` of the elements dropped from the window
The `while` cycle gets the maximum for the current window.

#### Score
| Runtime (ms) | - %     | O                   | Memory (Mb) | - %     | O             |
| ------------ | ------- | ------------------- | ----------- | ------- | ------------- |
| 1996         | 30.14 % | $\large O(Nlog(N))$ | 34.9        | 10.44 % | $\large O(k)$ |

##### Time complexity:
Practically, we a sorting the array of the size `k` and we are doing it `N` times.
##### Memory:
`pas` costs us $\large O(k)$
`win` - $\large O(k)$
`ans` - $\large O(N)$, but we can shrink it to $\large O(1)$ if we switch to `yield`


### Solution 2 (monotonic queue) (**[stolen](https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n))**)

```python
class Solution:
    def maxSlidingWindow(self, xs: List[int], k: int) -> List[int]:
        win = deque()
        ans = []
        for i, x in enumerate(xs):
            while win and xs[win[-1]] < x:
                win.pop()
            win.append(i)
            if win[0] == i - k:
                win.popleft()
            if i >= k - 1:
                ans.append(xs[win[0]])
        return ans
```

`win` - is the sliding window. We store it as a `deque`. It stores the indexes of the elements which can at some point become the maximums of the window.

`while win and xs[win[-1]] < x:` - when the new element arrives, we can safely drop all the smaller elements which arrived before it.

`win.append(i)` - actually there will be always indexes of the elements sorted (by values) in ascending order

`if win[0] == i - k:` - if the max element's index is out of the window's scope, we should drop it. We can only choose the first element in queue because **(1)** it will be the element with the smallest index, and **(2)** there can only be one element dropped at each `for` iteration (cause there can only be one element appended).

`if i >= k - 1:` - in the first `k-1` steps the window will be not full.

#### Score
| Runtime (ms) | - %      | O             | Memory (Mb) | - %     | O             |
| ------------ | -------- | ------------- | ----------- | ------- | ------------- |
| 1704         | 76.65  % | $\large O(N)$ | 30.3        | 36.32 % | $\large O(k)$ |



