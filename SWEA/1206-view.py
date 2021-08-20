import sys
sys.stdin = open('input.txt')

for i in range(1, 11):
    n = int(input())
    b = list(map(int, input().split()))  # buildings
    cnt = 0

    for idx in range(2, n-2):
        # highest building
        hb = max(b[idx-2], b[idx-1], b[idx+1], b[idx+2])
        if b[idx] > hb:
            cnt += (b[idx] - hb)

    print(f'#{i} {cnt}')
