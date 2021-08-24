import sys
sys.stdin = open('input.txt')


def get_winner(s, e):  # start, end
    if s == e:  # 부전승하는 경우
        return s

    w1 = get_winner(s, (s+e)//2)
    w2 = get_winner((s+e)//2 + 1, e)

    return w2 if (cards[w1], cards[w2]) in win2_cases else w1


for t in range(1, int(input())+1):
    n = int(input())
    cards = list(map(int, input().split()))
    win2_cases = [(1, 2), (2, 3), (3, 1)]

    result = get_winner(0, n-1)
    print(f'#{t} {result+1}')  # 학생 번호가 1부터 시작
