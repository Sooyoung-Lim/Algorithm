import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    square = [[0]*10 for _ in range(10)]
    total = 0

    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        for r in range(x1, x2+1):
            for c in range(y1, y2+1):
                square[r][c] += color

    for r in range(10):
       for c in range(10):
           if square[r][c] >= 3:
               total += 1
    # print(square)
    print('#{} {}'.format(tc, total))



