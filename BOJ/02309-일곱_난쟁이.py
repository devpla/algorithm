dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()
total = sum(dwarfs)

for i in range(9):
    for j in range(i+1,9):
        if total - (dwarfs[i]+dwarfs[j]) == 100:
            fakers = [i, j]

for i in range(9):
    if i not in fakers:
        print(dwarfs[i])
