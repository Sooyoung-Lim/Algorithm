import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    hour = h1+h2
    if hour > 12:
        hour -= 12
        if hour > 12:
            hour -= 12

    minute = m1 + m2
    if minute > 60:
        minute -= 60
        hour += 1

    print('#{} {} {}'.format(tc, hour, minute))

# 오류
# 9 30 6 50 -> 7 20
# 12 12 11 50 -> 13 2


