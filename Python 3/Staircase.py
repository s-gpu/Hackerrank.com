#!/usr/bin/python3

n = int(input())
for i in range(1, n):
    print(' ' * (n-i-1), '#' * i)
print('#' * n, end='')
