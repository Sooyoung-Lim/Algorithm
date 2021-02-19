import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # N 까지의 자연수를 원소로 갖는 리스트 생성
    main_list = list(i for i in range(1, 13))

    # 부분집합 전부 만들어서 리스트에 저장
    big_list = []
    for i in range(1<<len(main_list)):
        sub_list = []
        for j in range(len(main_list)):
            if i & (1<<j):
                sub_list.append(main_list[j])
        big_list.append(sub_list)
    # print(big_list)

    # 부분집합 중에서 원소의 갯수가 N개 인것만 추려서 리스트에 저장
    len_list = []
    for i in big_list:
        if len(i) == N:
            len_list.append(i)
    # print(len_list)

    # 합이 K이면 갯수 카운트
    result = 0
    for i in len_list:
        if sum(i) == K:
            result += 1

    print('#{} {}'.format(tc, result))
