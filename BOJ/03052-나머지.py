import sys
input = sys.stdin.readline

print(len(set([int(input())%42 for i in range(10)])))