#!/usr/bin/python

n = input()
for _ in xrange(n):
    i = input()
    if i >= 38 and i % 5 >= 3:
        i += 5 - (i % 5)
    print i
