import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N, Q = map(int, input().split())
    boxes = [0] * N

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        boxes[L-1:R] = [i] * (R-L+1)

    print(f'#{t}', *boxes)
