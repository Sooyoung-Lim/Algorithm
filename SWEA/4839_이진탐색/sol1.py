import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    l = 1
    r = P
    count_A = 0
    while P > 0:
        c = (l+r)//2
        count_A += 1
        if c == A:
            break
        elif c < A:
            l = c
        else:
            r = c
    # print(count_A)

    l = 1
    r = P
    count_B = 0
    while P > 0:
        c = (l + r) // 2
        count_B += 1
        if c == B:
            break
        elif c < B:
            l = c
        else:
            r = c
    # print(count_B)

    result = ''
    if count_A > count_B:
        result = 'B'
    elif count_A < count_B:
        result = 'A'
    else:
        result = 0

    print('#{} {}'.format(tc, result))
