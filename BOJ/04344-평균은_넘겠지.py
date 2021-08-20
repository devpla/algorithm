import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n_scores = list(map(int, input().split()))
    avg = sum(n_scores[1:])/n_scores[0]
    print(f'{len([score for score in n_scores[1:] if score > avg])/n_scores[0] * 100:.3f}%')