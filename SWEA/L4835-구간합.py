import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    sum_list = []

    for i in range(0, n-m+1):
        sum_list.append(sum(numbers[i:i+m]))

    result = max(sum_list) - min(sum_list)
    print(f'#{t} {result}')
