import sys
sys.stdin = open('input.txt')

# collections.Counter 없이 풀기
# max 안쓰고 풀기

for t in range(1, int(input())+1):
    n = int(input())
    numbers = list(map(int, input()))

    # 카운트 데이터를 넣을 리스트 초기화
    cnt_list = [0 for i in range(10)]

    for number in numbers:
        cnt_list[number] += 1

    max_idx = 0
    max_cnt = 0

    for idx, value in enumerate(cnt_list):
        # 가장 높은 인덱스로 갱신됨
        if value >= max_cnt:
            max_cnt = value
            max_idx = idx

    print(f'#{t} {max_idx} {max_cnt}')
