import sys
sys.stdin = open('input.txt')

money = (50000, 10000, 5000, 1000, 500, 100, 50, 10)

for t in range(1, int(input())+1):
    N = int(input())
    result = [0] * 8

    for i in range(8):
        result[i] = N // money[i]
        N %= money[i]

    print(f'#{t}')
    print(*result)
