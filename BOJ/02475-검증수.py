numbers = list(map(int, input().split()))

result = 0
for number in numbers:
    result += number ** 2
print(result % 10)