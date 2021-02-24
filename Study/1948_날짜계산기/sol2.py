import sys
sys.stdin=open('input.txt')

T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    temp = 0
    for i in range(1, m1):
        temp += dates[i]
    date1 = temp + d1
    temp = 0
    for i in range(1, m2):
        temp += dates[i]
    date2 = temp + d2
    result = date2 - date1 + 1
    print('#{} {}'.format(tc, result))