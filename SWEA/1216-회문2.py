import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    data = [input() for _ in range(100)]

    result = 0

    # 행
    for i in range(100):
        for j in range(100):
            for k in range(100-j+1):
                chars = data[i][j:j+k]
                if chars == chars[::-1]:
                    result = max(result, len(chars))

    # 열
    for j in range(100):
        chars = ''
        for i in range(100):
            chars += data[i][j]

        for k in range(100):
            for l in range(100-k+1):
                if chars[k:k+l] == chars[k:k+l][::-1]:
                    result = max(result, len(chars[k:k+l]))

    print(f'#{t} {result}')
