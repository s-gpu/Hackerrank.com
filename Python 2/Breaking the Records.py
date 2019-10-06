#!/usr/bin/python

n = input()
ar = map(int, raw_input().split())
res = [0, 0]
mx = ar[0]
mn = ar[0]
for i in xrange(1, n):
    m = ar[i]
    if m > mx:
        mx = m
        res[0] += 1
    elif m < mn:
        mn = m
        res[1] += 1
print res[0], res[1]
