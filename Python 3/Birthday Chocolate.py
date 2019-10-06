#!/usr/bin/python3

n = int(input())
s = list(map(int, input().split()))
d, m = list(map(int, input().split()))
res = 0
ar = s[:m-1]
for i in s[m-1:]:
    ar.append(i)
    if sum(ar) == d:
        res += 1
    ar.pop(0)
print(res)
