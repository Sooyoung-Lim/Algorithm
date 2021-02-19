import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(1, N+1):
    total = 0
    for x in str(i):
        if x in ['3','6','9']:
            total += 1
    if total == 0:
        print(i, end=' ')
    else:
        print('-'*total, end=' ')






