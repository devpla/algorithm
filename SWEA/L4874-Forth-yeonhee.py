import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    postfix_expr = list(input().split())
    stack = []

    try:
        for token in postfix_expr:
            if token.isdigit():
                stack.append(int(token))
            elif token == '.':
                result = stack.pop()
                if stack:
                    result = 'error'
            else:
                num2, num1 = stack.pop(), stack.pop()
                if token == '+': res = num1 + num2
                elif token == '*': res = num1 * num2
                elif token == '-': res = num1 - num2
                elif token == '/': res = num1 // num2
                stack.append(res)

    except:
        result = 'error'

    print(f'#{t} {result}')
