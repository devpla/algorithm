import sys
sys.stdin = open('input.txt')


DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def dfs(r, c, number):
    if len(number) == 7:
        result.add(number)
        return

    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, number + graph[nr][nc])


for t in range(1, int(input())+1):
    graph = [input().split() for _ in range(4)]
    result = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, graph[r][c])

    print(f'#{t} {len(result)}')
