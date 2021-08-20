def list_of_digits(n):
    if n < 10:
        return [n]
    return list_of_digits(n//10) + [n%10]

def is_arithmetic_sequence(n):
    numbers = list_of_digits(n)
    if len(numbers) == 1:
        return True
    else:
        gap = numbers[1] - numbers[0]
        for idx in range(1, len(numbers)):
            if numbers[idx] - numbers[idx-1] != gap:
                return False
        return True

cnt = 0
for i in range(1, int(input())+1):
    if is_arithmetic_sequence(i):
        cnt += 1

print(cnt)
