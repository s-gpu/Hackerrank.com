#!/usr/bin/python3

input()
ar = map(int, raw_input().split())
result = 0
m = max(ar)
for i in ar:
    if i == m:
        result += 1
print result
