#!/usr/bin/python3

n = int(input())
ar = list(map(int, input().split()))
result = [0, 0, 0]
for i in ar:
    if i > 0:
        result[0] += 1
    elif i < 0:
        result[1] += 1
    else:
        result[2] += 1
for i in range(3):
    print(result[i]/n)
