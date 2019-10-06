#!/usr/bin/python3

x1, v1, x2, v2 = list(map(int, input().split()))
for i in range(10000):
	if x1 == x2:
		print("YES")
		exit()
	x1 += v1
	x2 += v2
print("NO")
