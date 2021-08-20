# 일어나서 다시 풀기

N = int(input())

if N <= 1022:
    numbers = list(range(10))
    for i in range(1, 10):
        for j in range(0, i):
            numbers.append([10*i + j])
    if N <= 55:
        print(numbers[N])
    else:
        pass

# 0 ~ 9 : 10
# 10
# 20 21
# 30 31 32 
# 40 41 42 43
# 50 51 52 54 ...

# 210
# 310 320 321
# 410 420 421 430 431 432
# 510 520 521 530 531 532 540 541 542 543

# 3210

# 43210

