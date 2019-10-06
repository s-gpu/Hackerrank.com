#!/usr/bin/python

n, k = map(int, raw_input().split())
ar = map(int, raw_input().split())
res = 0
for i in xrange(n):
    for j in xrange(n):
        if i < j and (ar[i] + ar[j]) % k == 0:
            res += 1
print res
