import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{t} {max(numbers) - min(numbers)}')
