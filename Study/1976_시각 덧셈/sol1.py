import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    h_result = 0
    m_result = 0

    if h1 + h2 <= 12 and m1 + m2 < 60:
        h_result = h1 + h2
        m_result = m1 + m2
    elif h1 + h2 < 12 and m1 + m2 > 60:
        h_result = h1 + h2 + 1
        m_result = m1 + m2 - 60
    elif h1 + h2 >= 12 and m1 + m2 > 60:
        h_result = h1 + h1 - 12 + 1
        m_result = m1 + m2 - 60
    elif h1 + h2 > 12 and m1 + m2 < 60:
        h_result = h1 + h2 - 12
        m_result = m1 + m2
    elif h1 + h2 >= 23 and m1 + m2 < 60:
        h_result = h1 + h2 -24
        m_result = m1 + m2
    elif h1 + h2 >= 23 and m1 + m2 > 60:
        h_result = h1 + h2 - 24 + 1
        m_result = m1 + m2 - 60

    print('#{} {} {}'.format(tc, h_result, m_result))

# 방법 2) 방법 1에서 오류나길래 조건 다 나눠서 해봤다.
# 그래도 같은오류남


