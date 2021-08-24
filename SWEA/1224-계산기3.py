import sys
sys.stdin = open('input.txt')


def get_postfix(expr):
    isp = {'(': 0, '+': 1, '*': 2, }
    icp = {'(': 3, '+': 1, '*': 2, }
    stack = []
    postfix_expr = []

    for token in expr:
        if token.isdigit():
            postfix_expr.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix_expr.append(stack.pop())
            stack.pop()
        else:
            while stack and icp[token] <= isp[stack[-1]]:
                postfix_expr.append(stack.pop())
            stack.append(token)

    while stack:
        postfix_expr.append(stack.pop())

    return postfix_expr


for t in range(1, 11):
    n = int(input())
    math_expr = list(input())
    postfix_exp = get_postfix(math_expr)
    stack = []

    for token in postfix_exp:
        if token.isdigit():
            stack.append(int(token))
        else:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())

    print(f'#{t} {stack.pop()}')
