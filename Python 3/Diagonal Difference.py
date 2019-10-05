#!/usr/bin/python3

n = int(input())
ar = []
for _ in range(n):
    ar.append(list(map(int, input().split())))
s1 = 0; s2 = 0
for i in range(n):
    s1 += ar[i][i]
    s2 += ar[n-i-1][i]
print(abs(s1 - s2))
