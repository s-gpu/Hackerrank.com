#!/usr/bin/python3

s, t = list(map(int, input().split()))
a, b = list(map(int, input().split()))
input()
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))
r = 0
for i in apples:
    x = a + i
    if s <= x and x <= t:
        r += 1
print(r)
r = 0
for i in oranges:
    x = b + i
    if s <= x and x <= t:
        r += 1
print(r)
