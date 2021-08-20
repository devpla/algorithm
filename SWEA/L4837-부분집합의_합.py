import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    a = [i for i in range(1, 13)]
    result = 0

    for i in range(1 << 12):
        cnt = 0
        total = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                total += a[j]
        if cnt == n and total == k:
            result += 1

    print(f'#{t} {result}')
