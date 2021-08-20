import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    n = int(input())
    print(f'#{t}')

    for i in range(n):
        print(' '.join(str(11 ** i)))
