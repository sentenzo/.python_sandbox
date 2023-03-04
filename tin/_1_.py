##############

n = 10  # int(input())
words = "aaa aa aaa a a".split()  # input().split()
pattern = "YBYBYBYBBB"  # input()
#          ---**---*-
assert n == len(pattern)

i = 0
ans = 0
for word in words:
    m = len(word)
    for j in range(i + 1, i + m):
        if pattern[j] == pattern[j - 1]:
            ans += 1
            break
    i += m

print(ans)
