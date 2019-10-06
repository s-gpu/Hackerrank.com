#!/usr/bin/python3

n = int(input())
ar = list(map(int, input().split()))
res = [0] * (max(ar) - min(ar) + 1)
for i in ar:
    res[i-1] += 1
print(res.index(max(res)) + 1)
