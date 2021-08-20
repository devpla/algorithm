import sys
sys.stdin = open('input.txt', encoding='utf-8')
# 인코딩 하지 않으면 UnicodeDecodeError 발생

for _ in range(10):
    t, target, sentence = int(input()), input(), input()
    print(f'#{t} {sentence.count(target)}')
