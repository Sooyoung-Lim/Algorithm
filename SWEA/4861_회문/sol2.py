import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    matrix = []
    for i in range(N):
        matrix.append(list(input()))
    # print(matrix)

    for r in range(N):
        for c in range(N-M+1):
            row_list = matrix[r][c:c+M]
            if row_list == row_list[::-1] :
                result = row_list

    for r in range(N-M+1):
        for c in range(N):
            col_list =[]
            for i in range(M):
                col_list.append(matrix[r+i][c])
            if col_list == col_list[::-1] :
                result = col_list

    result = ''.join(result)
    print('#{} {}'.format(tc, result))


