import sys
sys.stdin = open('input.txt')

dr = (1, 1, -1, -1, 0)  # 인덱스 오류 방지
dc = (1, -1, -1, 1, 0)


def dfs(cnt, r, c, sr, sc, d):
    global result

    if d == 4:  # 방향을 네번 바꾼 경우
        return

    if (r, c) == (sr, sc):  # 도착시 값 갱신
        result = max(result, cnt)
        return

    if 0 <= r < N and 0 <= c < N and not dessert[graph[r][c]]:
        dessert[graph[r][c]] = 1
        dfs(cnt + 1, r + dr[d], c + dc[d], sr, sc, d)  # 원래 방향 그대로 이동
        dfs(cnt + 1, r + dr[d+1], c + dc[d+1], sr, sc, d+1)  # 방향 전환
        dessert[graph[r][c]] = 0


for t in range(1, int(input())+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dessert = [0]*101
    result = -1

    for i in range(N-2):
        for j in range(1, N-1):
            dessert[graph[i][j]] = 1
            dfs(1, i+1, j+1, i, j, 0)
            dessert[graph[i][j]] = 0

    print(f'#{t} {result}')
