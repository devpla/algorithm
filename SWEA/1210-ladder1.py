import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점에서 출발해서 시작점 찾음
    i = 99
    j = ladder[99].index(2)  # 도착지점

    # i가 0 즉, 출발 지점까지 오면 반복문 자동 종료
    while i > 0:
        # 이동 및 탐색 경로 0으로 바꿈
        ladder[i][j] = 0

        # 디음 목적 좌표 설정
        if j-1 >= 0 and ladder[i][j-1]:  # 왼쪽
            j -= 1
        elif j+1 < 100 and ladder[i][j+1]:  # 오른쪽
            j += 1
        elif i-1 >= 0:  # 위
            i -= 1

    print(f'#{t} {j}')
