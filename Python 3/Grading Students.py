#!/usr/bin/python3

n = int(input())
for _ in range(n):
    i = int(input())
    if i >= 38 and i % 5 >= 3:
        i += 5 - (i % 5)
    print(i)
