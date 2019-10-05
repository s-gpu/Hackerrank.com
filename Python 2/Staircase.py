#!/usr/bin/python3

n = input()
for i in xrange(1, n):
    print ' ' * (n-i-1), '#' * i
print '#' * n
