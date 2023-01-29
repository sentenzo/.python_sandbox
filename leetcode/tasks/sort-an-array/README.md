# LeetCode 912. Sort an Array

[link to LeetCode](https://leetcode.com/problems/sort-an-array/) (<span style="color:orange">medium</span>)

## Description
Given an array of integers `nums`, sort the array in ascending order.
## Constraints
-   `1 <= nums.length <= 5 * 104`
-   `-5 * 104 <= nums[i] <= 5 * 104`
## Examples
```python
>>> Solution().sort([5,1,1,2,0,0])
# [0,0,1,1,2,5]
```
## Abstract (TL;DR)
Seriously? You forgot how to do it? Shame on you!
## Thoughts
Ideally it should be done in-place and without additional memory allocation.

I've made a testing suit:

```python
from abc import ABC, abstractmethod
from random import choices

class SortAlgorithm(ABC):
    @staticmethod
    @abstractmethod
    def sort(xs: List[int]) -> None: pass

    @classmethod
    def test(cls, times: int = 1, size=150, elements=range(100)):
        if times < 1:
            return
        arr = choices(elements, k=size)
        sarr = arr[:]
        cls.sort(sarr)
        assert (sorted(arr) == sarr), sarr
        cls.test(times - 1)

class StdSort(SortAlgorithm):
    @staticmethod
    def sort(xs: List[int]) -> None:
        xs.sort()

class Solution:
    def sortArray(self, xs: List[int]) -> List[int]:
        Srt = StdSort # replace with: QuickSort, HeapSort, MargeSort
        # Srt.test(20)
        Srt.sort(xs)
        return xs
```


### Solution 1.0 (`QuickSort`)
My recent implementation:
```python
class QuickSort(SortAlgorithm):
    @staticmethod
    def sort(xs: List[int], a=0, b=None) -> None:
        b = len(xs) - 1 if b == None else b
        if b - a <= 0:
            return
        aa, bb = a, b
        piv = xs[(a + b) // 2 + 1]
        while a < b:
            if xs[a] < piv:
                a += 1
            elif xs[b] > piv:
                b -= 1
            else:
                xs[a], xs[b] = xs[b], xs[a]
                a += 1
        QuickSort.sort(xs, aa, a - 1)
        QuickSort.sort(xs, a, bb)
```

#### What's happening here
`a` and `b` are both included in the interval.

`piv` - is for "pivot".
`piv = xs[(a + b) // 2 + 1]` - `+ 1` in the end is extremely crucial. Without this `1` it would fall into an infinite recursion. 
Example: `sort(xs, 0, 1) => sort(xs, 0, 1) => ...`
Maybe the implementation with `[a,b)` would be better 🤷

`aa, bb = a, b` - to remember where we started.

`while a < b:` - we stop when `a == b`.
We are putting `a` and `b` in such positions that `xs[a] >= piv` and `xs[b] <= piv`, and then we swap: `xs[a], xs[b] = xs[b], xs[a]`.

This code is very sensitive to any changes unfortunately 😔
It would stop work if you:
- replace `a += 1` in `else:` with `b -= 1`:
	- `RecursionError: maximum recursion depth exceeded in comparison`
- swap `if` with `elif`:
	- is makes mistakes in sorting
- replace `QuickSort.sort` invokes of arguments `(xs, aa, a-1)`, `(xs, a, bb)` with:
	- `(xs, aa, a)`, `(xs, a, bb)` or `(xs, aa, a)`, `(xs, a + 1, bb)`  - `maximum recursion depth exceeded`
	- `(xs, aa, a - 1)`, `(xs, a + 1, bb)` - mistakes in sorting

### Solution 1.1 (`QuickSort` - old)
My working implementation for `05/07/2021 22:33`

The additional memory is used 😕
And there's also special condition for `xs[i] == pivot`.

```python
    def qsort(xs):        
        def pivoti(xs, a, b):
            m = (a + b) // 2
            am = xs[a] <= xs[m]
            mb = xs[m] <= xs[b - 1]
            ab = xs[a] <= xs[b - 1]
            
            if am == mb:
                pass
            elif am == (not mb):
                xs[m], xs[b - 1] = xs[b - 1], xs[m]
            else:
                xs[m], xs[a] = xs[a], xs[m]
            return m
            
        def partition(xs, a, b):
            p = pivoti(xs, a, b)
            pv = xs[p]
            l, m, r = [], [], []
            for i in range(a, b):
                e = xs[i]
                if e < pv:
                    l.append(e)
                elif e > pv:
                    r.append(e)
                else:
                    m.append(e)
            xs[a:b] = l + m + r
            return a + len(l), b - len(r)        
        
        def qsrt(xs, a, b):
            if b - a < 2:
                return
            elif b - a == 2:
                if xs[a] > xs[a + 1]:
                    xs[a],  xs[a + 1] = xs[a + 1], xs[a]
                return
            else:
                lm, rm = partition(xs, a, b)
                qsrt(xs, a, lm)
                qsrt(xs, rm, b)
                
        qsrt(xs, 0, len(xs))
        return xs
```

### Solution 2.0 (`HeapSort`)
Again my today's implementation goes first.
It's longer than the `QuickSort`, but more readable.

```python
class HeapSort(SortAlgorithm):
    @staticmethod
    def sort(xs: List[int], a=0, b=None) -> None:
        def par(i):
            return (i - 1) >> 1

        def chi(i):
            a = (i + 1) << 1
            return (a - 1, a)
        n = len(xs)
        def popup(i):
            if i == 0:
                return
            p = par(i)
            if xs[i] > xs[p]:
                xs[i], xs[p] = xs[p], xs[i]
                popup(p)

        def sink(i, bottom):
            ch1, ch2 = chi(i)
            if ch1 >= bottom:
                return
            if ch2 < bottom:
                ch_max = ch1 if xs[ch1] >= xs[ch2] else ch2
                if xs[ch_max] > xs[i]:
                    xs[i], xs[ch_max] = xs[ch_max], xs[i]
                    sink(ch_max, bottom)
            elif xs[ch1] > xs[i]:
                xs[i], xs[ch1] = xs[ch1], xs[i]

        for i in range(n):
            popup(i)

        l = n
        while l:
            l -= 1
            xs[0], xs[l] = xs[l], xs[0]
            sink(0, l)
```

#### What's happening here
We'll be making a max-heap.

`def par(i) -> int:` - returns parent of the given index.

`def chi(i) -> List[int]:` - returns children of the given index (two).

`def popup(i) -> None:` - pops the unheapified element up (recursively).

`def sink(i, bottom):` - drops the element down, but not deeper than the bottom (the end of the heap).

`for i in range(n): popup(i)` equals to `heapify(xs)`

`while l:` we are building the sorted (ascendant) array on the bottom of the max-heap:
```
  heap:   vvvvvvvvvvv
    xs:  [6 5 3 4 1 2 7 8 9]
sorted:               ^^^^^
```


### Solution 2.1 (`HeapSort`- old)
Also a max-heap solution. Quite similar to the previous actually.
```python
    def heapsort(xs):
        n = len(xs)
        if n < 2:
            return xs
        ch = lambda i: i * 2 + 1 
        pr = lambda i: (i - 1) // 2 
        def popup(i):
            if i > 0:
                pi = pr(i)
                if xs[pi] < xs[i]:
                    xs[i], xs[pi] = xs[pi], xs[i]
                    popup(pi)
        [popup(i) for i in range(n)]
        def sink(i, h):
            ci = ch(i)
            c0 = c1 = pr = xs[i]
            if ci <= h:
                c0 = xs[ci]
            if ci + 1 <= h:
                c1 = xs[ci + 1]
            if pr < c0 and c0 >= c1:
                xs[i], xs[ci] = xs[ci], xs[i]
                sink(ci, h)
            elif pr < c1:
                xs[i], xs[ci + 1] = xs[ci + 1], xs[i]
                sink(ci + 1, h)
        for i in range(1, n):
            xs[0], xs[n - i] = xs[n - i], xs[0]
            sink(0, n - i - 1)
        return xs
```

### Solution 3.0 (`MargeSort`)
This one was the easiest to implement. But it uses additional memory.

```python
class MargeSort(SortAlgorithm):
    @staticmethod
    def marge(xs: List[int], a, m, b) -> None:
        if b - a <= 1:
            return
        aa = a
        mm = m
        ans = []
        while True:
            if a == mm:
                xs[aa:aa + len(ans)] = ans
                return
            elif m == b:
                xs[aa:b] = ans + xs[a:mm]
                return
            else:
                if xs[a] <= xs[m]:
                    ans.append(xs[a])
                    a += 1
                else:
                    ans.append(xs[m])
                    m += 1

    @staticmethod
    def sort(xs: List[int], a=0, b=None) -> None:
        if b == None:
            b = len(xs)
        if b - a <= 1:
            return
        m = (b + a) // 2
        MargeSort.sort(xs, a, m)
        MargeSort.sort(xs, m, b)
        MargeSort.marge(xs, a, m, b)
```

The right border is not included: `[a,b)`

### Solution 3.1 (`MargeSort` - old, memory optimization)

It still consumes $O(N)$ memory in worst case, but it uses buffer (`stack`) to shrink it.
Yet somehow I can't see this economy on the test results.

```python
def margesort(xs):

	def marge(xs, a, m, b):
		stack = []
		i, j = a, m
		while True:
			if i >= m:
				if i + len(stack) == b:
					xs[i: b] = stack
					break
				elif len(stack) == 0:
					break
				elif stack[0] <= xs[j]:
					xs[i] = stack.pop(0)
				else:
					xs[i] = xs[j]
					j += 1
			else:
				if stack and stack[0] <= xs[j]:
					if xs[i] > stack[0]:
						stack.append(xs[i])
						xs[i] = stack.pop(0)
				elif xs[i] > xs[j]:
					stack.append(xs[i])
					xs[i] = xs[j]
					j += 1
			i += 1

	def msort(xs, a, b):
		if b - a > 1:
			m = (a + b) // 2
			msort(xs, a, m)
			msort(xs, m, b)
			marge(xs, a, m, b)

	a, b = 0, len(xs)
	msort(xs, a, b)
	return xs
```

### $O(N^2)$ algorithms

#### Insertion sort 
```python
arr =  [4 2 6 5 1 2]
i = 0 # ^ |
i = 1 #   ^
#     [4 2 6 5 1 2] 
# => ([4 # 6 5 1 2], 2) 
# => ([4 4 6 5 1 2], 2)
# =>  [2 4 6 5 1 2]
i = 2
#     [2 4 6 5 1 2]
# => ([2 4 # 5 1 2], 6) => [2 4 6 5 1 2]
i = 3
# [2 4 5 6 1 2]
i = 4
#    [2 4 5 6 # 2] => [2 4 5 6 6 2] => [2 4 5 5 6 2]
# => [2 4 4 5 6 2] => [2 2 4 5 6 2] => [1 2 4 5 6 2]
...
```
```python
def insort(xs):
	"""
	Insertion sort 
	"""

	i, n = 1, len(xs)
	while i < n:
		tmp = xs[i]
		j = i - 1
		while j >= 0:
			if xs[j] < tmp:
				break
			else:
				xs[j + 1] = xs[j]
				j -= 1
		xs[j + 1] = tmp
		i += 1
	return xs
```

#### Bubble sort (**[stolen](https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap)**)
```python
[*4 2 6 5 1 2] => [2 4 *6 ..] => [2 4 5 1 2 *6]
=> [2 4 *5 ..] => [2 4 1 2 *5 6]
=> [2 *4 ..] => [2 1 2 *4 5 6] 
...
```
```python
def bubbleSort(self, nums):
	n = len(nums)
	for i in range(n):
		for j in range(0, n - i - 1):
			if nums[j] > nums[j + 1]:
				nums[j], nums[j + 1] = nums[j + 1], nums[j]
```

#### Selection sort (**[stolen](https://leetcode.com/problems/sort-an-array/discuss/276916/Python-bubble-insertion-selection-quick-merge-heap)**)
```python
i  = min_ind(arr[0:])
arr[0], arr[i] = arr[i], arr[0]
i  = min_ind(arr[1:])
arr[1], arr[i + 1] = arr[i + 1], arr[1]
...
```
```python
def selectionSort(self, nums):
	for i in range(len(nums)):
		_min = min(nums[i:])
		min_index = nums[i:].index(_min)
		nums[i + min_index] = nums[i]
		nums[i] = _min
	return nums
```