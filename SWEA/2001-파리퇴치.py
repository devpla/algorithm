import sys
sys.stdin = open('input.txt')

# Brute Force
for t in range(1, int(input())+1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for i in range(n-m+1):
        for j in range(n-m+1):
            dead_flies = 0
            for di in range(m):
                for dj in range(m):
                    dead_flies += arr[i+di][j+dj]
            result.append(dead_flies)

    print(f'#{t} {max(result)}')
