#!/usr/bin/python3

n, k = list(map(int, input().split()))
ar = list(map(int, input().split()))
res = 0
for i in range(n):
    for j in range(n):
        if i < j and (ar[i] + ar[j]) % k == 0:
            res += 1
print(res)
