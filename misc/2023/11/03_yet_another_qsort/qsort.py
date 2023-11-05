from random import randint

TESTS = False

def i2n():
    return int(input())


def i2ns():
    return list(map(int, input().split()))


def partial(arr, left, right, pivot):
    eq_point = gt_point = uk_point = left
    lt_is_empty = eq_is_empty = gt_is_empty = True
    while uk_point < right:
        # lt_is_empty = (left == eq_point)
        # eq_is_empty = (eq_point == gt_point)
        # gt_is_empty = (gt_point == uk_point)

        if arr[uk_point] > pivot:
            if gt_is_empty:
                gt_is_empty = False
        elif arr[uk_point] == pivot:
            if not gt_is_empty:
                arr[gt_point], arr[uk_point] = arr[uk_point], arr[gt_point]
            else:
                pass  # do nothing
            gt_point += 1
            if eq_is_empty:
                eq_is_empty = False
        elif arr[uk_point] < pivot:
            if not eq_is_empty:
                if not gt_is_empty: 
                    arr[eq_point], arr[gt_point], arr[uk_point] = arr[uk_point], arr[eq_point], arr[gt_point]
                else: # gt_point == uk_point
                    arr[eq_point], arr[uk_point] = arr[uk_point], arr[eq_point]
            else:  # eq_point == gt_point
                if gt_is_empty:  # eq_point == gt_point == uk_point
                    pass  # do nothing
                else:
                    arr[gt_point], arr[uk_point] = arr[uk_point], arr[gt_point]

            eq_point += 1
            gt_point += 1
            if lt_is_empty:
                lt_is_empty = False
        uk_point += 1
    return eq_point, gt_point


def pick_pivot(arr, left, right):
    return arr[randint(left, right-1)]


def qsort(arr, left, right):
    if right - left < 2:
        return
    pivot = pick_pivot(arr, left, right)
    eq_point, gt_point = partial(arr, left, right, pivot)
    qsort(arr, left, eq_point)
    qsort(arr, gt_point, right)


def test(arr):
    arr_original = arr[:]
    arr_sorted = sorted(arr)
    qsort(arr_original, 0, len(arr_original))
    assert arr_sorted == arr_original, arr_original


def run_tests():
    def test(arr):
        arr_original = arr[:]
        arr_sorted = sorted(arr)
        qsort(arr_original, 0, len(arr_original))
        assert arr_sorted == arr_original, arr_original

    test([1, 5, 2, 4, 3])
    test([1, 2, 3, 4, 5])
    test([5, 3, 1, 2, 4])
    test([5, 4, 3, 2, 1])
    test([1, 5, 2, 4, 3])
    test([12])
    test([])
    test([6, 4, 2, 1, 3, 5])
    test([4, 4, 3, 4])
    test([5, 3, 1, 1, 4, 6])

def main():
    n = i2n()
    if n == 0:
        print()
        return
    arr = i2ns()
    qsort(arr, 0, n)
    print(*arr)

if TESTS:  
    run_tests()

    # import cProfile
    # cProfile.run("run_tests()")
else:
    main()