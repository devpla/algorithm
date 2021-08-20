N = int(input())
if N < 10:
    lst = [0, N, 0]
else:
    lst = [N//10, N%10, 0]

cnt = 0

while True:
    lst[2] = (lst[0] + lst[1]) % 10
    cnt += 1
    if 10 * lst[1] + lst[2] == N:
        break
    else:
        lst[0], lst[1] = lst[1], lst[2]

print(cnt)

