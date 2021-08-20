import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t, n = map(int, input().split())
    numbers = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    for i in range(0, n*2, 2):
        graph[numbers[i]].append(numbers[i+1])

    visited = [0 for _ in range(100)]
    stack = [0]

    while stack:  # dfs
        now = stack.pop()

        if not visited[now]:
            visited[now] = 1
            for v in graph[now]:
                if not visited[v]:
                    stack.append(v)

    print(f'#{t} {visited[99]}')
