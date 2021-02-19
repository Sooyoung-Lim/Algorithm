import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    text, pattern = input().split()

    M = len(text)
    N = len(pattern)

    count = 0
    i = 0
    while i <= M-N+1:
        if pattern == text[i:i+N]:
            count += 1
            i += N
        else:
            i += 1

    result = M - count * N + count
    print('#{} {}'.format(tc, result))


