N = int(input())
scores = list(map(int, input().split()))
max_value = max(scores)

print(sum(map(lambda score: score/max_value*100, scores))/len(scores))
