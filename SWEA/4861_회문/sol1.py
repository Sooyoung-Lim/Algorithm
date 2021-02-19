import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    matrix = [[input()] for _ in range(N)]
    print(matrix)

    # for i in range(N):
    #     for j in range(M):
    #         if matrix[0][i][j] == matrix[0][i][M-1-j]:
    #             result = matrix[0][i][j]
    #     print(result)
