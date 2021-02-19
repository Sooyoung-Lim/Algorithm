from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 칠할 영역의(사각형의) 갯수
    sq_list = [set({}), set({})]
    for n in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                sq_list[color-1].add((x,y))

    result = sq_list[0] & sq_list[1]
    print('#{} {}'.format(tc, len(result)))

