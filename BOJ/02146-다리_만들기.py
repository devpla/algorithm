import sys
from collections import deque
input = sys.stdin.readline

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs1(sr, sc, n):  # 섬 번호 매기기
    q = deque([(sr, sc)])
    graph[sr][sc] = n

    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == 1:
                graph[nr][nc] = n
                q.append((nr, nc))


def bfs2(n):  # 섬끼리 최단 거리 찾기
    global result

    dis = [[-1]*N for _ in range(N)]
    q = deque()

    for r in range(N):
        for c in range(N):
            if graph[r][c] == n:
                q.append((r, c))
                dis[r][c] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] and graph[nr][nc] != n:
                    result = min(result, dis[r][c])
                    return
                if not graph[nr][nc] and dis[nr][nc] == -1:
                    dis[nr][nc] = dis[r][c] + 1
                    q.append((nr, nc))


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
num = 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            num += 1
            bfs1(i, j, num)

result = float('inf')

for i in range(2, num):
    bfs2(i)

print(result)
