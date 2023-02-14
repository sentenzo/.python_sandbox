# 37. Sudoku Solver

[link to LeetCode](https://leetcode.com/problems/sudoku-solver/) (<span style="color:red">hard</span>)


## Description
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1.  Each of the digits `1-9` must occur exactly once in each row.
2.  Each of the digits `1-9` must occur exactly once in each column.
3.  Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

## Constraints
-   `board.length == 9`
-   `board[i].length == 9`
-   `board[i][j]` is a digit or `'.'`.
-   It is **guaranteed** that the input board has only one solution.
## Examples
**Input:**
```python
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
```
**Output:** 
```python
[["5","3","4","6","7","8","9","1","2"],
 ["6","7","2","1","9","5","3","4","8"],
 ["1","9","8","3","4","2","5","6","7"],
 ["8","5","9","7","6","1","4","2","3"],
 ["4","2","6","8","5","3","7","9","1"],
 ["7","1","3","9","2","4","8","5","6"],
 ["9","6","1","5","3","7","2","8","4"],
 ["2","8","7","4","1","9","6","3","5"],
 ["3","4","5","2","8","6","1","7","9"]]
```
## Abstract (TL;DR)
Depth-first search. Check validity of each step.
## Thoughts
### Solution 1 (DFS with classes)
```python
class Solution:    
    def solveSudoku(self, board: List[List[str]]) -> None:
        Sudoku(board).solve()

class Sudoku:
    @staticmethod
    def ij2k(i, j):
		"""
		Returns the list of chunk names by i, j.
		There are three types of chunks:
		 - row chunks
		 - column chunks
		 - box (3x3) chunks
		"""
        #return f"r{i}", f"c{j}", f"b{i//3}{j//3}" 
        return i, 10 + j, 100 + 10*(i // 3) + (j // 3)

    def setChunks(self, i, j, d, remove = False):
        v = 0 if remove else 1
        for k in Sudoku.ij2k(i, j):
            self.chunks[k][d] = v

    def __init__(self, board: List[List[str]]):
        self.board = board
        self.chunks = defaultdict(lambda: [0] * 9)
        self.empties = []
		# ↓↓ init chunks and empties
        for i, j in product(range(9), range(9)):
            d = board[i][j]
            if d == ".":
                self.empties.append((i, j))
            else:
                self.setChunks(i, j, int(d) - 1)
    
    def opts(self, i, j):
		"""
		What valid values can we put at (i,j)?
		"""
        ans = set(range(9))
        for k in Sudoku.ij2k(i, j):
            for a in list(ans):
                if self.chunks[k][a]:
                    ans.remove(a)
        return ans

    def solve(self) -> bool:
		# we start from the cells with 
		#   less variants to choose from
        self.empties.sort(key=lambda e: len(self.opts(*e)))
        
        def dfs(pos = 0):
            if pos == len(self.empties):
                return True
            i, j = self.empties[pos]
            for opt in self.opts(i, j):
                self.setChunks(i, j, opt)
                if dfs(pos + 1):
                    self.board[i][j] = str(opt + 1)
                    return True
                self.setChunks(i, j, opt, remove=True)
            return False

        return dfs()
```

The `self.empties.sort` grants almost double time shrinking.

#### Score
| Runtime (ms) | - %     | Memory (Mb) | - %     |
| ------------ | ------- | ----------- | ------- |
| 176          | 70.64 % | 14.5        | 28.47 % |

### Solution 2 (another DFS) ([**stolen**](https://leetcode.com/problems/sudoku-solver/discuss/140837/Python-very-simple-backtracking-solution-using-dictionaries-and-queue-~100-ms-beats-~90))
This one works slightly (20-30%) faster than mine. The memory consumption is the same.
```python
class Solution:
    def solveSudoku(self, board):
        rows, cols, triples, visit = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set), collections.deque([])
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    triples[(r // 3, c // 3)].add(board[r][c])
                else:
                    visit.append((r, c))
        def dfs():
            if not visit:
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for dig in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                if dig not in rows[r] and dig not in cols[c] and dig not in triples[t]:
                    board[r][c] = dig
                    rows[r].add(dig)
                    cols[c].add(dig)
                    triples[t].add(dig)
                    visit.popleft()
                    if dfs():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(dig)
                        cols[c].discard(dig)
                        triples[t].discard(dig)
                        visit.appendleft((r, c))
            return False
        dfs()
```

