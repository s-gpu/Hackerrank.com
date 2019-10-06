#!/usr/bin/python

n = input()
s = map(int, raw_input().split())
d, m = map(int, raw_input().split())
res = 0
ar = s[:m-1]
for i in s[m-1:]:
    ar.append(i)
    if sum(ar) == d:
        res += 1
    ar.pop(0)
print res
