import sys
sys.stdin = open('input.txt')

for i in range(1, int(input())+1):
    num = int(input())
    result = {i: 0 for i in [2, 3, 5, 7, 11]}

    for key in result.keys():
        while num % key == 0:
            num //= key
            result[key] += 1

    print(f'#{i}', *list(result.values()))
