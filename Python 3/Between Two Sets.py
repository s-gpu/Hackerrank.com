#!/usr/bin/python3

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
for i in range(max(a), min(b)+1):
    for j in a:
        if i % j != 0:
            break
    else:
        for j in b:
            if j % i != 0:
                break
        else:
            res += 1
print(res)
