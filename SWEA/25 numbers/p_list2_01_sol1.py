import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = 5
    matrix = [list(map(int, input().split())) for i in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    total = 0

    for r in range(N):
        for c in range(N):
            abs_sum = 0
            for d in range(4):
                center = matrix[r][c]
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < N and 0 <= nc < N:
                    around = matrix[nr][nc]
                    abs_sum += abs(center - around)
            total += abs_sum

    print("#{} {}".format(tc, total))







