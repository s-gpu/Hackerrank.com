#!/usr/bin/python

n = input()
ar = map(int, raw_input().split())
res = [0] * (max(ar) - min(ar) + 1)
for i in ar:
    res[i-1] += 1
print res.index(max(res)) + 1
