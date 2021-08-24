import sys
sys.stdin = open('input.txt')

MOVES = ((1, 0), (0, 1), (-1, 0), (0, -1))


def find_start():
    for r in range(n):
        for c in range(n):
            if maze[r][c] == '2':
                return r, c


def dfs(r, c):
    global result
    for dr, dc in MOVES:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            # 도착
            if maze[nr][nc] == '3':
                result = 1
            elif maze[nr][nc] == '0':
                visited[nr][nc] = 1
                dfs(nr, nc)


for t in range(1, int(input())+1):

    n = int(input())
    maze = [input().rstrip() for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    r, c = find_start()
    result = 0
    dfs(r, c)

    print(f'#{t}', result)
