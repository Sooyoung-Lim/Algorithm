import sys
sys.stdin = open('input.txt')

# s가 들어왔을 떄 가장 긴 회문의 길이 뽑는 함수
def solution(s):
    n = len(s)

    # 회문 판별
    # 회문이면 result에 append
    result = []
    for i in range(n):
        for j in range(n, i, -1):
            if s[i:i+j] == s[i:i+j][::-1]:
                result.append(s[i:i+j])

    # result 결과들 중에 제일 긴 길이 뽑기
    max_length = 0
    for word in result:
        if len(word) > max_length:
            max_length = len(word)

    return(max_length)
print(solution('looool'))



#
#
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     matrix = []
#     for i in range(N):
#         matrix.append(list(input()))
#     # print(matrix)
#
#     for r in range(N):
#         for c in range(N-M+1):
#             row_list = matrix[r][c:c+M]
#             if row_list == row_list[::-1] :
#                 result = row_list
#
#     for r in range(N-M+1):
#         for c in range(N):
#             col_list =[]
#             for i in range(M):
#                 col_list.append(matrix[r+i][c])
#             if col_list == col_list[::-1] :
#                 result = col_list
#
#     result = ''.join(result)
#     print('#{} {}'.format(tc, result))
#
#
