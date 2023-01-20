# Leetcode 121. Best Time to Buy and Sell Stock


[link to LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) <span style="color:green">(easy)</span>

## Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

## Constraints
-   `1 <= prices.length <= 10**5`
-   `0 <= prices[i] <= 10**4`
## Examples
### Example 1:
```python
prices = [7,1,5,3,6,4]
#           ^     ^
# ans : 6 - 1 == 5
>>> 5
```
### Example 1:
```python
prices = [7,6,4,3,1]
#                  ^^
>>> 0
```
## Abstract (TL;DR)
At each `i` compute the `min` for `prices[:i]` and check how much can you gain if you sale now. Do it in one pass. 
## Thoughts
It confused me a lot when I tried it 5 months ago.
I used recursion back then. It was a wrong approach.
```python
class Solution:
    def maxProfit(self, ps: List[int]) -> int:
		################
		# I worked on refining the seq
        i = 0
        for i in range(len(ps) - 1):
            if ps[i] < ps[i + 1]:
                break;
        ps = ps[i:]
		################
        if len(ps) <= 1: 
            return 0 
        min_index, min_value = min(enumerate(ps), key=lambda p: p[1])
        max_index, max_value = max(enumerate(ps), key=lambda p: p[1])
        if min_index <= max_index:
            return max_value - min_value
        if min_index > max_index:
            left  = ps[:max_index + 1]
            right = ps[max_index + 1:]
            return max(self.maxProfit(left), self.maxProfit(right))
```
Yet, it passed the tests (hardly):
#### Score
| Runtime (ms) | - %     | Memory (Mb) | - %     |
| ------------ | ------- | ----------- | ------- |
| 1132         | 23.66 % | 24.8        | 98.69 % |

The better approach looks like this:
### Solution 1 (one pass, DP)
#### Python
```python
class Solution:
    def maxProfit(self, ps: List[int]) -> int:
        low = 100_000
        ans = 0
        for p in ps:
            low = min(low, p)
            ans = max(ans, p - low)
        return ans
```
Funny - there's not so much of a difference in speed.
##### Score
| Runtime (ms) | - %     | Memory (Mb) | - %     |
| ------------ | ------- | ----------- | ------- |
| 1060         | 54.32 % | 25.2        | 52.50 % |

#### Java
It works 1000 times faster than the Python solution.
```java
class Solution {
    public int maxProfit(int[] prices) {
        int low = Integer.MAX_VALUE;
        int ans = 0;
        for (int i = 0; i < prices.length; i += 1) {
            int p = prices[i];
            if (low > p) {
                low = p;
            }
            int a = p - low;
            if (ans < a) {
                ans = a;
            }
        }
        return ans;
    }
}
```
##### Score
| Runtime (ms) | - %      | Memory (Mb) | - %     |
| ------------ | -------- | ----------- | ------- |
| 1            | 100.00 % | 51.9        | 79.27 % |

