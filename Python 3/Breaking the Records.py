#!/usr/bin/python3

n = int(input())
ar = list(map(int, input().split()))
res = [0, 0]
mx = ar[0]
mn = ar[0]
for i in range(1, n):
    m = ar[i]
    if m > mx:
        mx = m
        res[0] += 1
    elif m < mn:
        mn = m
        res[1] += 1
print(res[0], res[1])
