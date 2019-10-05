#!/usr/bin/python

n = input()
ar = map(int, raw_input().split())
result = [0, 0, 0]
for i in ar:
    if i > 0:
        result[0] += 1.00
    elif i < 0:
        result[1] += 1.00
    else:
        result[2] += 1.00
for i in xrange(3):
    print result[i]/n
