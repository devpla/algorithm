import sys
sys.stdin = open('input.txt')


DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


for t in range(1, int(input())+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N**2+1)

    for r in range(N):
        for c in range(N):
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if graph[nr][nc] == graph[r][c] + 1:
                        visited[graph[r][c]] = 1
                        break

    result_num, result, cnt = 0, 0, 0

    for i in range(N*N, -1, -1):
        if visited[i]:
            cnt += 1
        else:
            if result <= cnt:
                result = cnt
                result_num = i + 1
            cnt = 0

    print(f'#{t} {result_num} {result+1}')
