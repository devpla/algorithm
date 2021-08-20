import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    laser_between = input().split('()')  # 레이저를 기준으로 split
    stick = 0                            # 현재 쇠막대기의 수
    result = 0                           # 총 조각의 수

    # ['', '(((', '', ')(', ')', '))(', ')']
    for lb in laser_between:             # 리스트 내 요소(string) 접근
        for p in lb:                     # 요소(string) 내 괄호 하나하나 접근
            if p == '(':                 # 여는 괄호일 경우 : 현재 stick +1
                stick += 1
            elif p == ')':               # 닫는 괄호일 경우 : 현재 stick -1 및 최종 갯수 +1
                stick -= 1
                result += 1
        result += stick                  # for 문 이후 결정된 stick 값 더함

    print(f'#{t} {result}')
