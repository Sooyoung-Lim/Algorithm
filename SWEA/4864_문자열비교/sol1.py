import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    pattern = input()
    text = input()

    # print(pattern, text)
    if pattern in text:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))