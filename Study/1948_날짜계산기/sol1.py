import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    dates = list(map(int, input().split()))
    # 모든 월을 일로 바꿔서 연산할 것이다.
    # {월 : 1월1일을 기준으로 하는 일} 딕셔너리를 만든다
    # {0:0} 은 인덱스에러 방지를 위한 더미데이터
    dates_dict = {0:0,  1:31, 2:59, 3:90, 4:120, 5:151, 6:181, 7:212, 8:243, 9:273, 10:304, 11:334, 12:365}

    for key, val in dates_dict.items():
        # 첫번째 월정보를 일정보로 바꾼다. '해당 월의 전달의 일수'로!
        if dates[0] == key:
            dates[0] = dates_dict[key-1]
        # 두번째 월정보를 일정보로 바꾼다. '해당 월의 전달의 일수'로!
        if dates[2] == key:
            dates[2] = dates_dict[key-1]

    result = dates[2] + dates[3] - (dates[0] + dates[1]) + 1
    print('#{} {}'.format(tc, result))