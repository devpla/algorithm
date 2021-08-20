import sys
from collections import deque
sys.stdin = open('input.txt')

# 시험볼 때 collections 도 사용 불가인가요..?

for t in range(1, int(input())+1):
    n = int(input())
    num_lst = sorted(list(map(int, input().split())))
    num_deque = deque(num_lst)
    ordered_lst = []

    for i in range(n):
        if i % 2:
            ordered_lst.append(num_deque.popleft())
        else:
            ordered_lst.append(num_deque.pop())

    print(f'#{t}', *ordered_lst[:10])
