import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result1 = ''
    for j in range(N):
        for i in range(N-1, -1, -1):
            result1 += str(matrix[i][j])
        break
        for

    print(result1)
