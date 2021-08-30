N = int(input())
search_num = int(input())

snail = [[0] * N for _ in range(N)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
idx = N*N
i = 0
r, c = 0, 0

while idx > 0:
    snail[r][c] = idx

    r = r + directions[i][0]
    c = c + directions[i][1]

    idx -= 1

    if 0 > r or r >= N or 0 > c or c >= N or snail[r][c]:
        r = r - directions[i][0]
        c = c - directions[i][1]

        i = (i+1)%4

        r = r + directions[i][0]
        c = c + directions[i][1]


for row in snail:
    print(*row)

for r in range(N):
    for c in range(N):
        if snail[r][c] == search_num:
            print(r+1, c+1)
