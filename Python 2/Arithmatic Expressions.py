#!/usr/bin/python

import sys
sys.setrecursionlimit(15000)
ops = [lambda x,y: x + y, lambda x,y: x * y, lambda x,y: x - y]
op2s = ['+', '*', '-', '']
def exp(i, value, l):
    if i == n:
        return l if value % 101 == 0 else None
    if len(cache[i]) > 0 and value in cache[i]:
        return cache[i][value]
    for k in range(3):
        if exp(i + 1, ops[k](value, a[i]), l) != None:
            l[i - 1] = k
            cache[i][value] = l
            return l
    cache[i][value] = None
    return None
n = input()
a = map(int, raw_input().split())
cache = [{}] * n
l = exp(1, a[0], [3] * n)
for i in range(n):
    sys.stdout.write(str(a[i]))
    sys.stdout.write(op2s[l[i]])
sys.stdout.flush()
