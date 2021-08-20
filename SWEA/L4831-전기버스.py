import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    bus_stops = list(map(int, input().split()))

    # n개의 정류장 중 충전 가능한 경우 1, 불가능한 경우 0
    # bus_stops 가 [1, 3, 5, 7, 9] 일 경우 [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    # while 문 안에서 in 연산을 쓰지 않기 위함 (시간 복잡도 O(n))
    chargeable_stops = [0] * (n+1)
    for i in bus_stops:
        chargeable_stops[i] = 1

    cnt = 0  # 충전 횟수
    bus = k  # 이동중인 버스의 index
    prev = 0  # 직전에 충전했던 정류장

    while bus < n:
        if chargeable_stops[bus]:
            cnt += 1
            prev = bus
            bus += k
        else:  # k 만큼 이동했는데 해당 지점에 충전소가 없을 경우 이전 정류장으로 한 칸씩 이동
            bus -= 1
            # 만약 이전 경로에서 가장 가까운 충전소가 직전에 충전했던 정류장일 경우, 다음 경로로 이동 불가능
            if bus == prev:
                cnt = 0
                break

    print(f'#{t} {cnt}')
