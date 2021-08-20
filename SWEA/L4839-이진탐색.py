import sys
sys.stdin = open('input.txt')


def binary_search(target, start, end, cnt):  # 재귀로 이진탐색 구현
    mid = (start + end) // 2

    if mid == target:
        return cnt
    elif mid > target:
        cnt += 1
        return binary_search(target, start, mid, cnt)
    else:
        cnt += 1
        return binary_search(target, mid, end, cnt)


for t in range(1, int(input())+1):
    p, a, b = map(int, input().split())

    cnt_a = binary_search(a, 1, p, 0)
    cnt_b = binary_search(b, 1, p, 0)

    min_cnt = min(cnt_a, cnt_b)

    print(f'#{t}', end=' ')
    print(0 if cnt_a == cnt_b else 'A' if cnt_a == min_cnt else 'B')
