import sys
sys.stdin = open('input.txt')

def solution():
    for i in range(9):
        temp1 = []
        temp2 = []
        for j in range(9):
            if matrix[i][j] in temp1 or matrix[j][i] in temp2:
                return 0
            temp1 += [matrix[i][j]]  # 가로
            temp2 += [matrix[j][i]]  # 세로
            temp3 = []
            # 네모칸
            if i % 3 == 0 and j % 3 == 0:
                for idx in range(3):
                    for jdx in range(3):
                        if matrix[i+idx][j+jdx] in temp3:
                            return 0
                        temp3 += [matrix[i+idx][j+jdx]]
    return 1
T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, solution()))