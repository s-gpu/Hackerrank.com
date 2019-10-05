#!/usr/bin/python3

input()
ar = list(map(int, input().split()))
result = 0
m = max(ar)
for i in ar:
    if i == m:
        result += 1
print(result)
