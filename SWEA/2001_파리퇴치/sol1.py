import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    square = []
    for n in range(N):
        lst = list(map(int, input().split()))
        square.append(lst)

    max_sum = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            current_sum = 0
            for dr in range(M):
                for dc in range(M):
                    current_sum += square[r+dr][c+dc]
            if max_sum < current_sum:
                max_sum = current_sum
    print('#{} {}'.format(tc, max_sum))

