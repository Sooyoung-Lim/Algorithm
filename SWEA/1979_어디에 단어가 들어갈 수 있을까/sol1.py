from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    square = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if square[r][c] == 0:
                # 11101 인 경우 예외처리
                if cnt == K:
                    total += 1
                cnt = 0
                continue
            else:
                cnt += 1

        if cnt == K:
            total += 1

    for c in range(N):
        cnt = 0
        for r in range(N):
            if square[r][c] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
                continue
            else:
                cnt += 1

        if cnt == K:
            total += 1

    print('#{} {}'.format(tc, total))

