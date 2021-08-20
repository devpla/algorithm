import sys
sys.stdin = open('input.txt')

# 정렬 기준 만들기
numbers = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

for t in range(1, int(input())+1):
    tc, n = input().split()
    result = sorted(input().split(), key=lambda x: numbers[x])

    print(f'{tc}\n', *result)
