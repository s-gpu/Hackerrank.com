#!/usr/bin/python

a = map(int, raw_input().split())
b = map(int, raw_input().split())
result = [0, 0]
for i in range(3):
    if a[i] > b[i]:
        result[0] += 1
    elif b[i] > a[i]:
        result[1] += 1
print result[0], result[1]
