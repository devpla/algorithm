import sys

input = sys.stdin.readline

for _ in range(int(input())):
    
    R, S = input().split()
    R = int(R)

    for s in S:
        print(s * R, end = '')
        
    print()