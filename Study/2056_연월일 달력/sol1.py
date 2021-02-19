import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    dates = list(map(int, input()))
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year = dates[0:4]
    month = dates[4:6]
    day = dates[6:8]
    print(month)
    res = -1
    if 1<= month <=12 and 1<= day <=days_list[month-1]:
        res = dates[0:4] + '/' + dates[4:6] + '/' + dates[6:8]
    print('#{} {}'.format(tc, res))



