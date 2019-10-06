#!/usr/bin/python

s, t = map(int, raw_input().split())
a, b = map(int, raw_input().split())
raw_input()
apples = map(int, raw_input().split())
oranges = map(int, raw_input().split())
r = 0
for i in apples:
    x = a + i
    if s <= x and x <= t:
        r += 1
print r
r = 0
for i in oranges:
    x = b + i
    if s <= x and x <= t:
        r += 1
print r
