#!/usr/bin/python

x1, v1, x2, v2 = map(int, raw_input().split())
for i in xrange(10000):
	if x1 == x2:
		print "YES"
		exit()
	x1 += v1
	x2 += v2
print "NO"
