import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):  # 테스트 케이스
    arr = [[0]*10 for _ in range(10)]
    for n in range(int(input())):   # 색칠 영역
        r1, c1, r2, c2, color = map(int, input().split())

        # arr 에 색칠
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    result = 0
    for row in arr:  # arr 의 값이 3일 경우 보라색
        result += row.count(3)
    print(f'#{t} {result}')
