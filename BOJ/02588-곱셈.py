# date : 2021-07-16 

num1 = int(input())
num2 = int(input())

divide_num = num2

while divide_num > 0:
    print(num1 * (divide_num % 10))
    divide_num = divide_num // 10 

print(num1 * num2)