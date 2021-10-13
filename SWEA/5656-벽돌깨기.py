import sys
from collections import deque
sys.stdin = open('input.txt')

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))


def gravity():
    for c in range(W):
        stack = []
        for r in range(H):
            if graph[r][c]:
                stack.append(graph[r][c])
                graph[r][c] = 0
        row = H - 1
        while stack:
            graph[row][c] = stack.pop()
            row -= 1
    return


def bfs(sr, sc):
    cnt = 1
    visited = [[0]*W for _ in range(H)]
    visited[sr][sc] = 1
    q = deque([(sr, sc)])
    while q:
        r, c = q.popleft()
        power = graph[r][c]
        graph[r][c] = 0
        for dr, dc in delta:
            for p in range(1, power):
                nr = r + dr * p
                nc = c + dc * p
                if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc]:
                    if graph[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = 1
                        cnt += 1
    gravity()
    return cnt


def play_game(depth, bricks):
    global result, graph
    if depth == N or not bricks:
        result = min(result, bricks)
        return
    saved = [row[:] for row in graph]
    for c in range(W):
        for r in range(H):
            if graph[r][c]:
                cnt = bfs(r, c)
                play_game(depth + 1, bricks - cnt)
                graph = [row[:] for row in saved]
                break


for t in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    graph = []
    total = 0
    for h in range(H):
        graph.append(list(map(int, input().split())))
        for w in range(W):
            if graph[h][w]:
                total += 1

    result = float('inf')
    play_game(0, total)
    print(f'#{t} {result}')
