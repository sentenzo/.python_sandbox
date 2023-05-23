# 135. Candy


[link to LeetCode](https://leetcode.com/problems/candy/)
<span style="color:red">hard</span>

It's actually not so hard. I would assess it as medium.

## Description
You've got children standing in the line. Each child has some number associated to them representing the `rating` of this child. Your task is to distribute candies between children, following the rules:
- if two children are neighbors in the line and one of them has a bigger rating then another, the child with the smaller rating should be given with less amount of candies
- each child should get at least one candy

Return _the minimum number of candies you need to have to distribute the candies to the children_.
## Constraints
-   `n == ratings.length`
-   `1 <= n <= 2 * 10^4`
-   `0 <= ratings[i] <= 2 * 10^4`
## Examples
```python
s = Solution()
s.candy([6, 2, 1, 2, 4, 5]) == 15
# 		 3  2  1  2  3  4
s.candy([6, 2, 2, 2, 4]) == 7
# 		 2  1  1  1  2
s.candy([2, 2, 2, 0, 0]) == 6
# 		 1  1  2  1  1
s.candy([7, 1, 0, 3, 5, 6, 4, 9, 2, 8, 12]) == 24
# 		 3  2  1  2  3  4  1  2  1  2  3

```

## Abstract (TL;DR)
Go left-to-right. 
When you see ascending sequence, assign the correct number of candies starting from `1`.
Then go right-to-left and do the same.

## Thoughts
The first intuitive impulse was to do smth. like this:
```python
ans = [0]
for i in range(1, n):
    if ratings[i-1] > ratings[i]:
	    ans.append(ans[-1] - 1)
	else:
	    ans.append(ans[-1] + 1)
return sum([x - min(ans) + 1
    for x in ans])
```
... which didn't work so well. It yielded the wrong results on inputs like `[1,3,7,2,3]` (wrong `ans=[1,2,3,2,3]`, actual `ans=[1,2,3,1,2]`).

So I came to a concept of several key cases:
- growth: `[..., 4, 5, 6, ...]` -> `1,2,3` 
- decline: `[..., 3, 2, 1, ...]` -> `3,2,1`
- stagnation: `[..., 7, 7, 7, ...]` -> `1,1,1`
- ... all the possible combination of the first three

But I reject it due to its unreasonable complicity.

The final approach was to reproduce the sequence of actions one should do to obtain the sequence of candies manually.

```python
[7, 1, 0, 3, 5, 6, 4, 2]
   >()>()            >()
 1, 1, 1, 2, 3, 4, 1, 1
   <----             <-
 3  2  1           2  1
```
Oh, like I really believe I'll understand something of this gibberish in a week.

## Solution
```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans = [1]
        chk = []
# left-to-right
# we can calc the candy for
# non-descending ratings
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                ans.append(ans[-1] + 1)
            elif ratings[i - 1] == ratings[i]:
                ans.append(1)
            else: # ratings[i - 1] > ratings[i]:
                ans.append(1)
# memorizing descending ratings
                chk.append(i)
# right-to-left
        for i in chk[::-1]:
            if ans[i - 1] <= ans[i]:
                ans[i - 1] = ans[i] + 1
        return sum(ans)
```
