#!/usr/bin/python3

a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = [0, 0]
for i in range(3):
    if a[i] > b[i]:
        result[0] += 1
    elif b[i] > a[i]:
        result[1] += 1
print(result[0], result[1])
