import sys
sys.stdin = open('input.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, int(input())):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    cnt = 1
    i, j = 0, -1
    k = 0

    while cnt <= n*n:
        ni, nj = i + di[k], j + dj[k]

        if 0 <= ni < n and 0 <= nj < n and not arr[ni][nj]:
            arr[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj

        else:
            k = (k + 1) % 4

    print(f'#{t}')
    for row in arr:
        print(*row)
