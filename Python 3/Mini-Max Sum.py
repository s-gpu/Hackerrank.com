#!/usr/bin/python3

ar = list(map(int, input().split()))
a = sum(ar); b = max(ar); c = min(ar)
print(a-b, a-c)
