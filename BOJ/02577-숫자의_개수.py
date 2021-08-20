import sys
from collections import Counter
input = sys.stdin.readline

result = 1
for _ in range(3):
    result *= int(input())

cnt = Counter(str(result))

for i in range(10):
    print(cnt[str(i)] if cnt[str(i)] else 0)