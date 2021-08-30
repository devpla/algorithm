numbers = list(map(int, input().split()))
numbers.pop(numbers.index(max(numbers)))
print(max(numbers))
