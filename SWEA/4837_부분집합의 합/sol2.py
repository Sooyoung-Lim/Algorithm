import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 1~12 집합 A
    A = [i for i in range(1, 13)]

    count = 0
    # 2^N==1을 N만큼 민다
    for i in range(0, 1<<len(A)): # 2^N-1 까지
        result = 0
        my_pass = 0
        for j in range(len(A)): # 0~11
            if i & (1<<j): # 1을 j만큼 민다 -> 0001 0010 0100 1000 자릿수 검증
                my_pass += 1
                result += A[j] # 통과해야 추가됨
                # print(A[j], end=' ')

        if my_pass == N:
            if result == K:
                count += 1

    print('#{} {}'.format(tc, count))
    # 왜 틀렸을까요?????