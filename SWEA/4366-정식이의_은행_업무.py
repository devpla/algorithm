import sys
sys.stdin = open('input.txt')


def num_to_dec(num: list, notation: int):
    tmp = 0
    for n, value in enumerate(num[::-1]):
        tmp += value * notation**n
    return tmp


def check(num: list, notation: int):
    # decimal_num = int(num, notation)
    decimal_num = num_to_dec(num, notation)

    for n, value in enumerate(num[::-1]):
        for j in range(notation):
            if value == j:
                continue
            tmp = decimal_num - value * notation**n + j * notation**n

            if tmp not in num_list:
                num_list.add(tmp)
            else:
                return tmp


for t in range(1, int(input())+1):
    bi = list(map(int, input()))  # 이진수
    tr = list(map(int, input()))  # 삼진수
    # bi를 한비트씩만 바꾼 숫자를 넣는 리스트
    num_list = set()
    check(bi, 2)
    print(f'#{t} {check(tr, 3)}')
