#!/usr/bin/python

raw_input()
a = map(int, raw_input().split())
b = map(int, raw_input().split())
res = 0
for i in xrange(max(a), min(b)+1):
    for j in a:
        if i % j != 0:
            break
    else:
        for j in b:
            if j % i != 0:
                break
        else:
            res += 1
print res
