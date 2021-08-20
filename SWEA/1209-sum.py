import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    down_right_sum = 0  # 우하향 대각선
    down_left_sum = 0  # 좌하향 대각선

    for i in range(100):
        row_sum = 0  # 행
        col_sum = 0  # 열

        # 행의 합, 열의 합은 이중 for 문을 이용
        for j in range(100):
            row_sum += arr[i][j]
            col_sum += arr[j][i]

        # 각 행/열의 합을 구할 때마다 최댓값 갱신 / max 사용하지 않을 경우 비교문..
        max_sum = max(max_sum, row_sum, col_sum)

        # 단일 for 문 안에서는 대각선의 합 구함
        down_right_sum += arr[i][i]
        down_left_sum += arr[i][99-i]

    # 대각선의 합까지 고려한 최댓값
    max_sum = max(max_sum, down_right_sum, down_left_sum)

    print(f'#{t} {max_sum}')
