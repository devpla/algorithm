import sys
sys.stdin = open('input.txt')

for i in range(1, 11):
    n = int(input())  # 덤프 가능 횟수
    boxes = list(map(int, input().split()))

    for _ in range(n):
        max_idx = boxes.index(max(boxes))
        min_idx = boxes.index(min(boxes))

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    result = max(boxes) - min(boxes)
    print(f'#{i} {result}')
