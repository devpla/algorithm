# date : 2021-07-17

import sys
T = int(input())

for i in range(1, T + 1):
    a,b = map(int, sys.stdin.readline().split())
    print(f'Case #{i}: {a + b}')