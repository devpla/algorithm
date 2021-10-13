import sys
sys.stdin = open('input.txt')


def dfs(n):
    global result
    if n == N:
        return
    if sum(checked) == N//2:
        food_a = [i for i in range(N) if checked[i]]
        food_b = [i for i in range(N) if not checked[i]]
        result = min(result, abs(get_taste(food_a) - get_taste(food_b)))
        return

    checked[n] = 1
    dfs(n+1)
    checked[n] = 0
    dfs(n+1)


def get_taste(ingredients):
    taste = 0
    for i in ingredients:
        for j in ingredients:
            taste += table[i][j]
    return taste


for t in range(1, int(input())+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    checked = [0]*N
    dfs(0)
    print(f'#{t} {result}')
