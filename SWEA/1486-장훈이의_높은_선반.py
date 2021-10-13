import sys
sys.stdin = open('input.txt')


def dfs(idx, height):
    global result

    if height - B > result:
        return

    if idx == N:
        if height >= B:
            result = min(result, height - B)
        return

    dfs(idx+1, height + staff[idx])  # 해당 idx의 점원을 포함한 경우
    dfs(idx+1, height)               # 포함하지 않은 경우


for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    staff = list(map(int, input().split()))
    result = float('inf')
    dfs(0, 0)
    print(f'#{t} {result}')
