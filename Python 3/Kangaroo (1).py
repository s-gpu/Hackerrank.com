#!/usr/bin/python3

x1, v1, x2, v2 = list(map(int, input().split()))
v = (v2 - v1)
x = (x1 - x2)
if v != 0:
	x = x / v
	if x >=0 and x == int(x) and x <= 10000:
		print("YES")
	else:
		print("NO")
else:
	print("NO")
