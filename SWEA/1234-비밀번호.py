import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n, numbers = input().split()
    stack = []

    for num in numbers:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)

    print(f'#{t}', ''.join(stack))
