# 123. Best Time to Buy and Sell Stock III


[link to LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
<span style="color:red">hard</span>


## Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Constraints
-   `1 <= prices.length <= 10**5`
-   `0 <= prices[i] <= 10**5`
## Examples
| Input               | Output |
| ------------------- | ------ |
| `[3,3,5,0,0,3,1,4]` | `6`    |
| `[1,2,3,4,5]`       | `4`    |
| `[7,6,4,3,1]`       | `0`    |
| `[1]`               | `0`    |

## Abstract (TL;DR)
The approach is the same as in [Leetcode 714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/).

We are keeping track on four values:
- `full_0` - the max amount of funds if at this point in time we bought stocks, but only once
- `empty_0` - the max amount of funds if we soled stocks for the first time
- `full_1` - bought for the second time
- `empty_1` - sold for the second time

The state changes like this: `full_0 => empty_0 => full_1 => empty_1`.

At each step we've got a new `cur_price`. 
1. We check if we can sell it for the second time. This is a `full_1 => empty_1` transition: 
`empty_1 = max(empty_1, full_1 + cur_price)`
1. We check if we buy it for the second time (`empty_0 => full_1`):
`full_1 = max(full_1, empty_0 - cur_price)`
1. If we can sell it for the first time (`full_0 => empty_0`):
`empty_0 = max(empty_0, full_0 + cur_price)`
1. If we buy it first time:
`full_0 = max(full_0, -cur_price)`

The init values are:
`full_0 = full_1 = float("-inf")` - it is impassible to sell at the first move.
`empty_0 = empty_1 = 0` - the max previous profit is zero.

The answer is: 
`max(empty_0, empty_1)` - there can be two (`empty_1`) or one (`empty_0`) or zero (`empty_1` and `empty_0` stay `0` from the beginning) transactions.

## Thoughts
### Solution 1 (DP)

```python
class Solution:
    def maxProfit(self, ps: List[int]) -> int:
        f0 = f1 = float("-inf")
        e0 = e1 = 0
        for p in ps:
            e1 = max(e1, f1 + p)
            f1 = max(f1, e0 - p)
            e0 = max(e0, f0 + p)
            f0 = max(f0, -p)
		return e1 # max(e1, e0)
```
