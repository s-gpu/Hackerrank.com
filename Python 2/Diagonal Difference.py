#!/usr/bin/python

n = input()
ar = []
for _ in xrange(n):
    ar.append(map(int, raw_input().split()))
s1 = 0; s2 = 0
for i in xrange(n):
    s1 += ar[i][i]
    s2 += ar[n-i-1][i]
print abs(s1 - s2)
