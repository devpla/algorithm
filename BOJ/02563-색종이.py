import sys
input = sys.stdin.readline

paper = [[0]*100 for _ in range(100)]

for _ in range(int(input())):
    col, row = map(int, input().split())

    for i in range(10):
        for j in range(10):
            paper[row+i][col+j] = 1

print(sum(map(sum, paper)))
