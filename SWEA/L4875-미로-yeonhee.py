import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[0] * n for _ in range(n)]
    result = 0

    # 시작 인덱스 찾기
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                visited[r][c] = 1
                stack = [(r, c)]

    # 미로 찾기
    while stack:
        r, c = stack.pop()
        if maze[r][c] == 3:
            result = 1
            break
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and maze[nr][nc] in (0, 3):
                stack.append((nr, nc))
                visited[nr][nc] = 1

    print(f'#{t} {result}')
