import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))

    result = 0
    for i in range(len(N)):
        if N[i] % 2:
            result += N[i]
    print('#{} {}'.format(tc, result))
