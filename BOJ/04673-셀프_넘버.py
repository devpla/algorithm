def sum_of_digits(n):
    if n < 10:
        return n
    return n%10 + sum_of_digits(n//10)
    
def d(n):
    return n + sum_of_digits(n)

numbers = []
for i in range(1, 10001):
    numbers.append(d(i))

for i in range(1, 10001):
    if i not in numbers:
        print(i) 