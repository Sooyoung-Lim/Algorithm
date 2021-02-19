import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 정수의 갯수
    # M: 구간의 길이
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    # 구간별로 M개씩 더한거 넣어줄 빈 리스트 선언
    result_list = []
    # M개씩 끊어서 더할꺼니까 range의 마지막 값은 N-M+1
    for i in range(N-M+1):
        # M개씩 더해준 값 저장하기 위해 result 선언
        result = 0
        # i 번째부터 M개를 더한 값을 result 변수에 저장
        for j in range(i, i+M):
            result += numbers[j]
        # 그 result를 구간별로 다 보기 위해 하나씩 result_list에 넣어준다
        result_list.append(result)

    diff = max(result_list) - min(result_list)
    print('#{} {}'.format(tc, diff))