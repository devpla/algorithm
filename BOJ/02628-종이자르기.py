import sys
input = sys.stdin.readline

r, c = map(int, input().split())
r_list = []
c_list = []

for _ in range(int(input())):
    is_row, num = map(int, input().split())

    if is_row:
        r_list.append(num)
    else:
        c_list.append(num)

r_list = [0] + sorted(r_list) + [r]
c_list = [0] + sorted(c_list) + [c]


c_max = 0
r_max = 0

for i in range(len(c_list)-1):
    c_max = max(c_max, c_list[i+1] - c_list[i])

for i in range(len(r_list)-1):
    r_max = max(r_max, r_list[i+1] - r_list[i])

print(c_max * r_max)
