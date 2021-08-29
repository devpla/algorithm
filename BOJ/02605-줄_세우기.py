import sys
input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
order = [1]

for i in range(1, n):
    order[i-students[i]:i-students[i]] = [i+1]

print(*order)
