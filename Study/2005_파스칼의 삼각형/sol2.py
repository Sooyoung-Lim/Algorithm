import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 이 리스트 만드는것이 핵심
    my_list = [[0] * (i+1) for i in range(N)]

    for i in range(N):
        for j in range(i+1):
            # 첫행과 두번째 행은 모두 1
            if i == 0 or i == 1:
                my_list[i][j] = 1
            else:
                #가장 왼쪽열과 오른쪽 열은 1, 그 외 가운데 숫자들 연산
                my_list[i][0] = 1
                my_list[i][j-1] = my_list[i-1][j-2] + my_list[i-1][j-1]
                my_list[i][i] = 1

    # 출력이 까다롭다
    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(list(map(str, my_list[i]))))