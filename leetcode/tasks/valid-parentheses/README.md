# Leetcode 20. Valid Parentheses


[link to LeetCode](https://leetcode.com/problems/valid-parentheses/) (<span style="color:green">easy</span>)

## Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
## Constraints
-   `1 <= s.length <= 104`
-   `s` consists of parentheses only `'()[]{}'`.
## Examples
| Input      | Output  |
| ---------- | ------- |
| `"()"`     | `true`  |
| `"()[]{}"` | `true`  |
| `"(]"`     | `false` |
| `"([)]"`   | `false` |
| `"{[]}"`   | `true`  |

## Abstract (TL;DR)
Stack. The `ch in "[({"` is a push-command. Having `ch in "])]"` makes the stack do pop and check.

## Thoughts

### Solution 1 (stack)
Just now:
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p != {"}":"{", "]":"[", ")":"("}[c]:
                    return False
        return len(stack) == 0
```
10 months ago:
```python
class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = dict(zip(")}]", "({["))
        for c in s:
            if c in "({[":
                st.append(c)
            elif len(st) == 0 or d[c] != st.pop():
                return False
        return len(st) == 0
```

### Solution 2 (replace) ([**stolen**](https://leetcode.com/problems/remove-invalid-parentheses/discuss/75028/Short-Python-BFS))

This guy, [StefanPochmann](https://leetcode.com/StefanPochmann/) is very creative.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        p, n = len(s) + 1, len(s)
        while p - n:
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
            p, n = n, len(s)
        return s == ""
```
yet this solution is almost twice slower than mine.