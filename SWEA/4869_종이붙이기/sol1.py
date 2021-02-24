import sys
sys.stdin=open('sample_input.txt')

def dp(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return dp(n-1) + 2*dp(n-2)

T = int(input())
for tc in range(1, T+1):
    width = int(input())
    result = dp(width/10)
    print('#{} {}'.format(tc, result))

