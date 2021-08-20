import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = 0
    total_score = 0
    for data in input():
        if data == 'O':
            score += 1
        else:
            score = 0
        total_score += score
    print(total_score)