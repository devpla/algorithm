import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    a, b = input().split()
    result = a.count(b)
    a = a.replace(b, '')
    result += len(a)
    print(f'#{t} {result}')
