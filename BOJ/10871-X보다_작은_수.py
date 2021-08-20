# date : 2021-07-17
import sys
n, x = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = ""

for i in range(n):
    if numbers[i] < x:
        result += f'{numbers[i]} '

print(result[:-1])