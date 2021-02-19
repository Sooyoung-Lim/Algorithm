from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # step 1) N x N 행렬을 만들고 모두 0로 채운다음, 필요한 부분만 1로 바꿔
    matrix = [[0]*N for _ in range(N)]
    for i in range(N):
        matrix[i][0] = 1
        matrix[i][i] = 1

    # step 2) 파스칼 삼각형을 만든다
    for i in range(2, N):
        for j in range(1, i):
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
    # print(DataFrame(matrix))

    # step 3) 필요없는 나머지 0들을 지우고 출력한다.
    # 여기서 막힘
    for list in matrix:
        for number in list:
            if number == 0:
                number = ''
    print(DataFrame(matrix))

